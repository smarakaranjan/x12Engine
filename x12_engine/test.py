from x12_engine.registry.base import Registry
from x12_engine.core.context import X12Context
from x12_engine.mappers.x837p import ClaimMapper, map_to_edi_payload
from x12_engine.core.engine import X12Engine
from x12_engine.registry.x837p.loops import LOOPS
from x12_engine.registry.x837p.segments import SEGMENTS, ELEMENTS


# Initialize registry/context/mapper
registry = Registry(SEGMENTS, LOOPS, ELEMENTS)
context = X12Context()
mapper = ClaimMapper(registry)

# Initialize engine
engine = X12Engine('XHFMTYRSAJFLWHY', 'XHFMTYRSAJFLWHZ', 'XHFMTYRSAJFLWHN')

# data = {
#     "service_details_rendering_provider": "1",
#     "service_details_npi_code": "2",
#     "service_details_billing_provider": "1",
#     "service_details_billing_provider_npi_code": "2",
#     "service_details_other_provider": "1",
#     "service_details_place_of_service": "12",
#     "service_details_facility": {
#         "name": "11 - Office_edited"
#     },
#     "service_details_start_date": "2026-01-11T18:30:00Z",
#     "service_details_end_date": "2026-01-12T18:30:00Z",
#     "service_details_hospital_admit_date": "2026-01-12T18:30:00Z",
#     "service_details_date_injury": "2026-01-12T18:30:00Z",
#     "service_details_prior_auth": "12",
#     "patient_firstname": "John",
#     "patient_middlename": "M",
#     "patient_lastname": "Mathews",
#     "patient_dob": "2026-01-12",
#     "patient_client_id": "1",
#     "patient_gender": "Male",
#     "patient_phone_number": "06454564545",
#     "patient_address": "Check 123",
#     "insurance_primary": "test",
#     "insurance_plan_name": "test",
#     "insurance_plan_type": "Commercial",
#     "insurance_id": "1",
#     "insurance_group_id": "1",
#     "insurance_effective_date": "2026-01-13",
#     "insurance_eligibility": "2",
#     "insurance_claim_address": "Check 123",
#     "Guarantor": "1",
#     "charges_payment_date": "2026-01-12T18:30:00Z",
#     "charges_payment_type": "copay",
#     "charges_payment_amount": "150",
#     "charges_payment_method": "cash",
#     "services": [
#         {
#             "billing_code": {
#                 "cpt_code": "1sdfsg",
#                 "description": "Healthcare Management managements."
#             },
#             "modifier": {
#                 "modifier_code": "﻿﻿GQ",
#                 "description": "﻿GQ,Via asynchronous telecommunications system"
#             },
#             "icd_diagnoses": [
#                 {
#                     "code": "﻿A01",
#                     "description": "﻿A01 - Typhoid and paratyphoid fevers."
#                 }
#             ],
#             "ndc_code": {
#                 "code": "﻿﻿0002-0152-01",
#                 "description": "0002-0152-01 - 1 VIAL, SINGLE-DOSE in 1 CARTON (0002-0152-01)  / .5 mL in 1 VIAL, SINGLE-DOSE"
#             },
#             "start_date": "2026-01-11T18:30:00Z",
#             "end_date": "2026-01-12T18:30:00Z",
#             "quantity": "2",
#             "units": "Bytes",
#             "billed_charge": None
#         },
#         {
#             "billing_code": {
#                 "cpt_code": "81246",
#                 "description": "81246"
#             },
#             "modifier": {
#                 "modifier_code": "U2",
#                 "description": "U2,level of care 2"
#             },
#             "icd_diagnoses": [
#                 {
#                     "code": "A02",
#                     "description": "A02 - Other salmonella infections"
#                 }
#             ],
#             "ndc_code": {
#                 "code": "0002-0213-02",
#                 "description": "1 VIAL, MULTI-DOSE in 1 CARTON (0002-0213-01)  / 3 mL in 1 VIAL, MULTI-DOSE"
#             },
#             "start_date": "2026-01-18T18:30:00Z",
#             "end_date": "2026-01-20T18:30:00Z",
#             "quantity": "3",
#             "units": "Hours",
#             "billed_charge": None
#         }
#     ]
# }


data = {
    "id": 13,
    "created_by_name": "Jack Parker",
    "changed_by_name": None,
    "services": [
        {
            "id": 14,
            "billing_code": {
                "cpt_code": "1sdfsg",
                "description": "Healthcare Management managements."
            },
            "modifier": {
                "description": "GQ,Via asynchronous telecommunications system",
                "modifier_code": "GQ"
            },
            "icd_diagnoses": [
                {
                    "code": "A01",
                    "description": "A01 - Typhoid and paratyphoid fevers."
                }
            ],
            "ndc_code": {
                "code": "0002-0152-01",
                "description": "0002-0152-01 - 1 VIAL, SINGLE-DOSE in 1 CARTON (0002-0152-01)  / .5 mL in 1 VIAL, SINGLE-DOSE"
            },
            "start_date": "2026-01-08T18:30:00Z",
            "end_date": "2026-01-12T18:30:00Z",
            "quantity": "12",
            "units": "Bytes",
            "billed_charge": None,
            "superbill": 13
        }
    ],
    "service_details_rendering_provider": "1",
    "service_details_npi_code": "12",
    "service_details_billing_provider": "1",
    "service_details_billing_provider_npi_code": "2",
    "service_details_other_provider": "1",
    "service_details_place_of_service": "11",
    "service_details_facility": {
        "name": "Jul-15",
        "address": ""
    },
    "service_details_start_date": "2026-01-08T18:30:00Z",
    "service_details_end_date": "2026-01-12T18:30:00Z",
    "service_details_hospital_admit_date": "2026-01-08T18:30:00Z",
    "service_details_date_injury": "2026-01-12T18:30:00Z",
    "service_details_prior_auth": "12",
    "Guarantor": "1",
    "charges_payment_date": None,
    "charges_payment_type": None,
    "charges_payment_amount": None,
    "charges_payment_method": None,
    "check_details": None,
    "card_type": None,
    "card_number": None,
    "other_payment_method": None,
    "charges_notes": None,
    "patient_firstname": "John",
    "patient_lastname": "Doe",
    "patient_dob": "2026-01-09",
    "patient_client_id": "21",
    "patient_gender": "Male",
    "patient_phone_number": "06454564545",
    "patient_address": "Check 123",
    "insurance_primary": "test",
    "insurance_plan_name": "test",
    "insurance_plan_type": "Commercial",
    "insurance_id": "1",
    "insurance_group_id": "1",
    "insurance_effective_date": "2026-01-09",
    "insurance_eligibility": "2",
    "insurance_claim_address": "Check 123",
    "created_at": "2026-01-12T10:33:19.208562Z",
    "changed_at": "2026-01-12T10:33:19.208562Z",
    "service_notes": None,
    "created_by": 693,
    "changed_by": None
}

payload = map_to_edi_payload(data)

# Example payload
# payload = {
#     "interchange": {
#         "ISA06": "SENDERID      ",
#         "ISA08": "RECEIVERID    ",
#         "ISA09": "240123",
#         "ISA10": "1200",
#     },
#     "group": {
#         "GS02": "SENDERID",
#         "GS03": "RECEIVERID"
#     },
#     "1000A": {
#         "NM1": {"NM101": "41", "NM102": "2", "NM103": "SUBMITTER"},
#         "PER": {"PER01": "IC", "PER02": "5555555555"}
#     },
#     "1000B": {
#         "NM1": {"NM101": "40", "NM102": "2", "NM103": "RECEIVER"}
#     },
#     "2000B": [
#         {
#             "HL": {"HL01": "1", "HL03": "22"},
#             "SBR": {"SBR01": "P", "SBR02": "18"},
#             "NM1": {"NM101": "IL", "NM102": "1", "NM103": "DOE", "NM104": "JOHN"},
#             "N3": {"N301": "123 MAIN ST"},
#             "N4": {"N401": "ANYTOWN", "N402": "NY", "N403": "12345"},
#             "DMG": {"DMG01": "D8", "DMG02": "19800101", "DMG03": "M"},
#             "2300": [
#                 {
#                     "CLM": {"CLM01": "12345", "CLM02": "500"},
#                     "DTP": {"DTP01": "472", "DTP02": "D8", "DTP03": "20260112"},
#                     "2400": [
#                         {"LX": {"LX01": "1"}, "SV1": {"SV101": "HC:99213"}}
#                     ]
#                 }
#             ]
#         }
#     ]
# }

edi_string = engine.build_837p(payload)
print(edi_string)
