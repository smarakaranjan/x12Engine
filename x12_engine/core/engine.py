# x12_engine/core/engine.py

from datetime import datetime
from x12_engine.core.segment import Segment
from x12_engine.core.loop import Loop
from x12_engine.registry.x837p.segments import create_segment
from x12_engine.registry.x837p.loops import LOOPS
from x12_engine.registry.x837p.elements import ELEMENTS
from x12_engine.errors import (
    RequiredElementMissing, InvalidElementType,
    ElementOverflow, ElementUnderflow,
    LoopRepeatExceeded, ControlMismatch
)

class X12Engine:
    def __init__(self, sender_id, receiver_id, payer_id=None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.payer_id = payer_id

        # Control numbers
        self.isa_control = 1
        self.gs_control = 1
        self.st_control = 1

        # Segments buffer
        self.segments = []

    # -------------------------------
    # Control number helpers
    # -------------------------------
    def next_isa_control(self):
        val = self.isa_control
        self.isa_control += 1
        return str(val).zfill(9)

    def next_gs_control(self):
        val = self.gs_control
        self.gs_control += 1
        return str(val)

    def next_st_control(self):
        val = self.st_control
        self.st_control += 1
        return str(val).zfill(4)

    # -------------------------------
    # Element validation
    # -------------------------------
    def validate_element(self, segment_id, element):
        value = getattr(element, "value", "")
        if element.spec["required"] and not value:
            raise RequiredElementMissing(segment=segment_id, element=element.spec["id"])

        if value:
            if element.spec["type"] in ["N0", "R"] and not str(value).replace('.', '').isdigit():
                raise InvalidElementType(segment=segment_id, element=element.spec["id"], value=value, expected_type=element.spec["type"])

            if len(str(value)) > element.spec["max"]:
                raise ElementOverflow(segment=segment_id, element=element.spec["id"], value=value, max_len=element.spec["max"])

            # if len(str(value)) < element.spec["min"]:
            #     raise ElementUnderflow(segment=segment_id, element=element.spec["id"], value=value, min_len=element.spec["min"])

    # -------------------------------
    # Render segment
    # -------------------------------
    def render_segment(self, segment):
        # validate elements
        for el in segment.elements:
            self.validate_element(segment.segment_id, el)
        
        # include segment ID at the beginning
        values = [segment.segment_id] + [str(getattr(el, "value", "")) for el in segment.elements]
        return "*".join(values) + "~"


    # -------------------------------
    # Render loop recursively
    # -------------------------------
    def render_loop(self, loop, data):
        rendered = []
        instances = data.get(loop.loop_id, [])
        if not isinstance(instances, list):
            instances = [instances]

        if len(instances) > loop.max_repeat:
            raise LoopRepeatExceeded(loop_id=loop.loop_id, max_repeat=loop.max_repeat)

        for instance in instances:
            for child in getattr(loop, "children", []):
                # Case 1: Segment object
                if isinstance(child, Segment):
                    seg_data = instance.get(child.segment_id, {})
                    for el in child.elements:
                        el.value = seg_data.get(el.spec["id"], "")
                    rendered.append(self.render_segment(child))

                # Case 2: Nested Loop object
                elif hasattr(child, "loop_id"):
                    rendered.extend(self.render_loop(child, instance))

                else:
                    raise TypeError(f"Unknown child type in loop '{loop.loop_id}': {type(child)}")

        return rendered




    # -------------------------------
    # Build full 837P EDI
    # -------------------------------
    def build_837p(self, payload):
        """
        payload: dict containing keys matching loop IDs (1000A, 2000B, 2300, etc.)
        Example:
        payload = {
            "1000A": {"NM1": {...}, "PER": {...}},
            "2000B": [...],  # subscriber loops
            "2300": [...],   # claim loops
        }
        """
        edi = []

        # --- ISA ---
        isa = create_segment("ISA")
        isa_values = {
            "ISA01": "00",
            "ISA02": "          ",
            "ISA03": "00",
            "ISA04": "          ",
            "ISA05": "ZZ",
            "ISA06": self.sender_id.ljust(15),
            "ISA07": "ZZ",
            "ISA08": self.receiver_id.ljust(15),
            "ISA09": datetime.now().strftime("%y%m%d"),
            "ISA10": datetime.now().strftime("%H%M"),
            "ISA11": "U",
            "ISA12": "00401",
            "ISA13": self.next_isa_control(),
            "ISA14": "0",
            "ISA15": "P",
            "ISA16": ">"
        }
        for el in isa.elements:
            el.value = isa_values.get(el.spec['id'], "")
        edi.append(self.render_segment(isa))

        # --- GS ---
        gs = create_segment("GS")
        gs_values = {
            "GS01": "HC",
            "GS02": self.sender_id,
            "GS03": self.receiver_id,
            "GS04": datetime.now().strftime("%Y%m%d"),
            "GS05": datetime.now().strftime("%H%M"),
            "GS06": self.next_gs_control(),
            "GS07": "X",
            "GS08": "005010X222A1"
        }
        for el in gs.elements:
            el.value = gs_values.get(el.spec["id"], "")
        edi.append(self.render_segment(gs))

        # --- ST ---
        st = create_segment("ST")
        st_values = {
            "ST01": "837",
            "ST02": self.next_st_control(),
            "ST03": "005010X222A1"
        }
        for el in st.elements:
            el.value = st_values.get(el.spec["id"], "")
        edi.append(self.render_segment(st))

        # --- Render all top-level loops ---
        for loop_id, loop in LOOPS.items():
            if loop_id in payload:
                edi.extend(self.render_loop(loop, payload))

        # --- SE ---
        se = create_segment("SE")
        se_values = {
            "SE01": str(len(edi) + 1),  # number of included segments
            "SE02": st_values["ST02"]
        }
        for el in se.elements:
            el.value = se_values.get(el.spec["id"], "")
        edi.append(self.render_segment(se))

        # --- GE ---
        ge = create_segment("GE")
        ge_values = {
            "GE01": "1",
            "GE02": gs_values["GS06"]
        }
        for el in ge.elements:
            el.value = ge_values.get(el.spec["id"], "")
        edi.append(self.render_segment(ge))

        # --- IEA ---
        iea = create_segment("IEA")
        iea_values = {
            "IEA01": "1",
            "IEA02": isa_values["ISA13"]
        }
        for el in iea.elements:
            el.value = iea_values.get(el.spec["id"], "")
        edi.append(self.render_segment(iea))

        # Return full EDI string
        return "\n".join(edi)
