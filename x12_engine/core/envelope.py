from x12_engine.registry.x837p.segments import create_segment

class EnvelopeBuilder:
    """Build envelope segments"""
    def __init__(self, context):
        self.ctx = context

    def isa(self, data):
        seg = create_segment("ISA")
        for el in seg.elements:
            el.value = data.get(el.id, "")
        return seg

    def gs(self, data):
        seg = create_segment("GS")
        for el in seg.elements:
            el.value = data.get(el.id, "")
        return seg

    def st(self):
        seg = create_segment("ST")
        st_values = {
            "ST01": "837",
            "ST02": self.ctx.next_st(),
            "ST03": "005010X222A1"
        }
        for el in seg.elements:
            el.value = st_values.get(el.id, "")
        return seg
