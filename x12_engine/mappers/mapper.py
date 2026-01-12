def map_to_edi_payload(data):
    """
    Converts a healthcare claim JSON payload into an EDI 837P engine-friendly payload.
    Only maps supported loops/segments: ISA/GS, 1000A/B, 2000B, 2300, 2400
    """
    # -----------------------
    # Interchange / Group
    # -----------------------
    edi_payload = {
        "interchange": {
            "ISA06": data.get("service_details_rendering_provider", "SENDERID")[:15].ljust(15),
            "ISA08": data.get("service_details_other_provider", "RECEIVERID")[:15].ljust(15),
            "ISA09": data.get("service_details_start_date", "260112").replace("-", "")[2:],
            "ISA10": data.get("service_details_start_date", "1417")[11:16].replace(":", ""),
        },
        "group": {
            "GS02": data.get("service_details_rendering_provider", "SENDERID"),
            "GS03": data.get("service_details_other_provider", "RECEIVERID")
        },
        # -----------------------
        # Submitter / Receiver
        # -----------------------
        "1000A": {
            "NM1": {"NM101": "41", "NM102": "2", "NM103": "SUBMITTER"},
            "PER": {"PER01": "IC", "PER02": data.get("patient_phone_number", "")}
        },
        "1000B": {
            "NM1": {"NM101": "40", "NM102": "2", "NM103": "RECEIVER"}
        },
        # -----------------------
        # Patient / Subscriber
        # -----------------------
        "2000B": []
    }

    # 2000B loop (Patient)
    patient_loop = {
        "HL": {"HL01": "1", "HL03": "22"},
        "SBR": {
            "SBR01": "P",
            "SBR02": data.get("insurance_eligibility", "18"),  # example
            "SBR03": data.get("insurance_plan_name", ""),
            "SBR04": data.get("insurance_plan_type", ""),
            "SBR05": data.get("insurance_group_id", "")
        },
        "NM1": {
            "NM101": "IL",
            "NM102": "1",
            "NM103": data.get("patient_lastname", ""),
            "NM104": data.get("patient_firstname", ""),
            "NM105": data.get("patient_middlename", "")
        },
        "N3": {"N301": data.get("patient_address", "")},
        "N4": {
            "N401": "ANYTOWN",  # default, can be extended
            "N402": "NY",
            "N403": "12345"
        },
        "DMG": {
            "DMG01": "D8",
            "DMG02": data.get("patient_dob", "").replace("-", ""),
            "DMG03": "M" if data.get("patient_gender", "").upper() == "MALE" else "F"
        },
        # -----------------------
        # Claim / 2300 loop
        # -----------------------
        "2300": [
            {
                "CLM": {
                    "CLM01": "1",  # Claim number
                    "CLM02": data.get("charges_payment_amount", "0")
                },
                "DTP": {
                    "DTP01": "472",
                    "DTP02": "D8",
                    "DTP03": data.get("service_details_start_date", "").replace("-", "")
                },
                "2400": []
            }
        ]
    }

    # 2400 loop (service lines)
    for idx, service in enumerate(data.get("services", []), start=1):
        service_line = {
            "LX": {"LX01": str(idx)},
            "SV1": {
                "SV101": service.get("billing_code", {}).get("cpt_code", ""),
                "SV102": service.get("quantity", "1"),
                "SV103": service.get("units", ""),
            },
            "HI": {}
        }

        # ICD diagnoses
        for i, diag in enumerate(service.get("icd_diagnoses", []), start=1):
            service_line["HI"][f"HI{i:02d}"] = diag.get("code", "")

        # Optional NDC
        ndc = service.get("ndc_code", {}).get("code")
        if ndc:
            service_line["NDC"] = {"NDC01": ndc}

        patient_loop["2300"][0]["2400"].append(service_line)

    edi_payload["2000B"].append(patient_loop)

    return edi_payload
