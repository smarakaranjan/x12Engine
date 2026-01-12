# x12_engine/mappers/x837p.py

from datetime import datetime

from x12_engine.registry.x837p.loops import LOOPS
from x12_engine.registry.x837p.segments import create_segment
from x12_engine.errors import RequiredElementMissing, ElementOverflow, InvalidElementType

class ClaimMapper:
    """
    Maps a business payload (claims/subscribers/patients/services) to X12 segments
    and writes to X12Writer.
    """
    def __init__(self, registry):
        self.registry = registry

    def map_loop(self, loop_id, loop_data, writer):
        """
        Recursively write a loop and its nested loops.
        loop_data: dict or list of dicts
        """
        loop = self.registry.loop(loop_id)
        instances = loop_data
        if not isinstance(loop_data, list):
            instances = [loop_data]

        if len(instances) > loop.max_repeat:
            from x12_engine.errors import LoopRepeatExceeded
            raise LoopRepeatExceeded(loop_id=loop_id, max_repeat=loop.max_repeat)

        for instance in instances:
            # Render each segment in the loop
            for seg_id in loop.segments:
                seg_data = instance.get(seg_id, {})
                segment = create_segment(seg_id)
                for el in segment.elements:
                    el.value = seg_data.get(el.id, "")
                writer.write(segment.render())

            # Recursively render nested loops
            for nested_loop in getattr(loop, "nested_loops", []):
                if nested_loop.id in instance:
                    self.map_loop(nested_loop.id, instance[nested_loop.id], writer)

    def map(self, payload, writer):
        """
        Map entire payload dictionary to segments.
        Expected payload keys: 1000A, 1000B, 2000B, 2300, 2400, etc.
        """
        for loop_id in LOOPS:
            if loop_id in payload:
                self.map_loop(loop_id, payload[loop_id], writer)



# def map_to_edi_payload(data):
#     """
#     Converts a healthcare claim JSON payload into an EDI 837P engine-friendly payload.
#     Only maps supported loops/segments: ISA/GS, 1000A/B, 2000B, 2300, 2400
#     """
#     # -----------------------
#     # Interchange / Group
#     # -----------------------
#     edi_payload = {
#         "interchange": {
#             "ISA06": data.get("service_details_rendering_provider", "SENDERID")[:15].ljust(15),
#             "ISA08": data.get("service_details_other_provider", "RECEIVERID")[:15].ljust(15),
#             "ISA09": data.get("service_details_start_date", "260112").replace("-", "")[2:],
#             "ISA10": data.get("service_details_start_date", "1417")[11:16].replace(":", ""),
#         },
#         "group": {
#             "GS02": data.get("service_details_rendering_provider", "SENDERID"),
#             "GS03": data.get("service_details_other_provider", "RECEIVERID")
#         },
#         # -----------------------
#         # Submitter / Receiver
#         # -----------------------
#         "1000A": {
#             "NM1": {"NM101": "41", "NM102": "2", "NM103": "SUBMITTER"},
#             "PER": {"PER01": "IC", "PER02": data.get("patient_phone_number", "")}
#         },
#         "1000B": {
#             "NM1": {"NM101": "40", "NM102": "2", "NM103": "RECEIVER"}
#         },
#         # -----------------------
#         # Patient / Subscriber
#         # -----------------------
#         "2000B": []
#     }

#     # 2000B loop (Patient)
#     patient_loop = {
#         "HL": {"HL01": "1", "HL03": "22"},
#         "SBR": {
#             "SBR01": "P",
#             "SBR02": data.get("insurance_eligibility", "18"),  # example
#             "SBR03": data.get("insurance_plan_name", ""),
#             "SBR04": data.get("insurance_plan_type", ""),
#             "SBR05": data.get("insurance_group_id", "")
#         },
#         "NM1": {
#             "NM101": "IL",
#             "NM102": "1",
#             "NM103": data.get("patient_lastname", ""),
#             "NM104": data.get("patient_firstname", ""),
#             "NM105": data.get("patient_middlename", "")
#         },
#         "N3": {"N301": data.get("patient_address", "")},
#         "N4": {
#             "N401": "ANYTOWN",  # default, can be extended
#             "N402": "NY",
#             "N403": "12345"
#         },
#         "DMG": {
#             "DMG01": "D8",
#             "DMG02": data.get("patient_dob", "").replace("-", ""),
#             "DMG03": "M" if data.get("patient_gender", "").upper() == "MALE" else "F"
#         },
#         # -----------------------
#         # Claim / 2300 loop
#         # -----------------------
#         "2300": [
#             {
#                 "CLM": {
#                     "CLM01": "1",  # Claim number
#                     "CLM02": data.get("charges_payment_amount", "0")
#                 },
#                 "DTP": {
#                     "DTP01": "472",
#                     "DTP02": "D8",
#                     "DTP03": data.get("service_details_start_date", "").replace("-", "")
#                 },
#                 "2400": []
#             }
#         ]
#     }

#     # 2400 loop (service lines)
#     for idx, service in enumerate(data.get("services", []), start=1):
#         service_line = {
#             "LX": {"LX01": str(idx)},
#             "SV1": {
#                 "SV101": service.get("billing_code", {}).get("cpt_code", ""),
#                 "SV102": service.get("quantity", "1"),
#                 "SV103": service.get("units", ""),
#             },
#             "HI": {}
#         }

#         # ICD diagnoses
#         for i, diag in enumerate(service.get("icd_diagnoses", []), start=1):
#             service_line["HI"][f"HI{i:02d}"] = diag.get("code", "")

#         # Optional NDC
#         ndc = service.get("ndc_code", {}).get("code")
#         if ndc:
#             service_line["NDC"] = {"NDC01": ndc}

#         patient_loop["2300"][0]["2400"].append(service_line)

#     edi_payload["2000B"].append(patient_loop)

#     return edi_payload



def edi_date(value):
    """Convert ISO date → CCYYMMDD"""
    if not value:
        return ""
    return datetime.fromisoformat(value.replace("Z", "")).strftime("%Y%m%d")


def edi_time(value):
    """Convert ISO datetime → HHMM"""
    if not value:
        return ""
    return datetime.fromisoformat(value.replace("Z", "")).strftime("%H%M")


def map_to_edi_payload(data):
    """
    Maps Superbill JSON → EDI-engine-friendly 837P payload
    Supported loops only:
    ISA / GS
    1000A / 1000B
    2000B
    2300
    2400
    """

    edi_payload = {
        # ------------------------------------------------
        # Interchange / Group
        # ------------------------------------------------
        "interchange": {
            "ISA06": str(data.get("service_details_rendering_provider", "SENDER")).ljust(15),
            "ISA08": str(data.get("service_details_other_provider", "RECEIVER")).ljust(15),
            "ISA09": edi_date(data.get("created_at"))[2:],   # YYMMDD
            "ISA10": edi_time(data.get("created_at")),
        },
        "group": {
            "GS02": data.get("service_details_rendering_provider", "SENDER"),
            "GS03": data.get("service_details_other_provider", "RECEIVER"),
        },

        # ------------------------------------------------
        # 1000A – Submitter
        # ------------------------------------------------
        "1000A": {
            "NM1": {
                "NM101": "41",
                "NM102": "2",
                "NM103": data.get("created_by_name", "SUBMITTER"),
            },
            "PER": {
                "PER01": "IC",
                "PER02": data.get("patient_phone_number", ""),
            },
        },

        # ------------------------------------------------
        # 1000B – Receiver
        # ------------------------------------------------
        "1000B": {
            "NM1": {
                "NM101": "40",
                "NM102": "2",
                "NM103": "RECEIVER",
            }
        },

        # ------------------------------------------------
        # 2000B – Subscriber
        # ------------------------------------------------
        "2000B": [],
    }

    # ===============================
    # Subscriber Loop
    # ===============================
    subscriber_loop = {
        "HL": {
            "HL01": "1",
            "HL03": "22",
        },
        "SBR": {
            "SBR01": "P",
            "SBR02": "18",  # Self
            "SBR03": data.get("insurance_plan_name", ""),
            "SBR04": data.get("insurance_plan_type", ""),
            "SBR05": data.get("insurance_group_id", ""),
        },
        "NM1": {
            "NM101": "IL",
            "NM102": "1",
            "NM103": data.get("patient_lastname", ""),
            "NM104": data.get("patient_firstname", ""),
        },
        "N3": {
            "N301": data.get("patient_address", ""),
        },
        "N4": {
            "N401": "ANYTOWN",
            "N402": "NY",
            "N403": "12345",
        },
        "DMG": {
            "DMG01": "D8",
            "DMG02": edi_date(data.get("patient_dob")),
            "DMG03": "M" if data.get("patient_gender") == "Male" else "F",
        },
        "2300": [],
    }

    # ===============================
    # Claim Loop (2300)
    # ===============================
    claim = {
        "CLM": {
            "CLM01": f"CLM{data.get('id')}",
            "CLM02": data.get("charges_payment_amount") or "0",
        },
        "DTP": {
            "DTP01": "472",
            "DTP02": "D8",
            "DTP03": edi_date(data.get("service_details_start_date")),
        },
        "2400": [],
    }

    # ===============================
    # Service Lines (2400)
    # ===============================
    for index, service in enumerate(data.get("services", []), start=1):
        sv1 = {
            "SV101": f"HC:{service['billing_code']['cpt_code']}",
            "SV102": service.get("quantity", "1"),
        }

        # Modifiers
        modifier = service.get("modifier", {}).get("modifier_code")
        if modifier:
            sv1["SV101"] += f":{modifier}"

        service_line = {
            "LX": {"LX01": str(index)},
            "SV1": sv1,
        }

        # Diagnosis codes
        diagnoses = service.get("icd_diagnoses", [])
        if diagnoses:
            hi = {}
            for i, diag in enumerate(diagnoses, start=1):
                hi[f"HI{i:02d}"] = diag.get("code")
            service_line["HI"] = hi

        claim["2400"].append(service_line)

    subscriber_loop["2300"].append(claim)
    edi_payload["2000B"].append(subscriber_loop)

    return edi_payload