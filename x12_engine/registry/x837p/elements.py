# ELEMENTS = {
#     # Interchange Control Header (ISA)
#     "ISA01": {"id":"ISA01", "type":"ID", "min":2, "max":2, "required":True},
#     "ISA02": {"id":"ISA02", "type":"AN", "min":10, "max":10, "required":True},
#     "ISA03": {"id":"ISA03", "type":"ID", "min":2, "max":2, "required":True},
#     "ISA04": {"id":"ISA04", "type":"AN", "min":10, "max":10, "required":True},
#     "ISA05": {"id":"ISA05", "type":"ID", "min":2, "max":2, "required":True},
#     "ISA06": {"id":"ISA06", "type":"AN", "min":15, "max":15, "required":True},
#     "ISA07": {"id":"ISA07", "type":"ID", "min":2, "max":2, "required":True},
#     "ISA08": {"id":"ISA08", "type":"AN", "min":15, "max":15, "required":True},
#     "ISA09": {"id":"ISA09", "type":"DT", "min":6, "max":6, "required":True},
#     "ISA10": {"id":"ISA10", "type":"TM", "min":4, "max":4, "required":True},
#     "ISA11": {"id":"ISA11", "type":"ID", "min":1, "max":1, "required":True},
#     "ISA12": {"id":"ISA12", "type":"ID", "min":5, "max":5, "required":True},
#     "ISA13": {"id":"ISA13", "type":"AN", "min":9, "max":9, "required":True},
#     "ISA14": {"id":"ISA14", "type":"ID", "min":1, "max":1, "required":True},
#     "ISA15": {"id":"ISA15", "type":"ID", "min":1, "max":1, "required":True},
#     "ISA16": {"id":"ISA16", "type":"ID", "min":2, "max":2, "required":True},

#     # Functional Group Header (GS)
#     "GS01": {"id":"GS01", "type":"ID", "min":2, "max":2, "required":True},
#     "GS02": {"id":"GS02", "type":"AN", "min":2, "max":15, "required":True},
#     "GS03": {"id":"GS03", "type":"AN", "min":2, "max":15, "required":True},
#     "GS04": {"id":"GS04", "type":"DT", "min":8, "max":8, "required":True},
#     "GS05": {"id":"GS05", "type":"TM", "min":4, "max":8, "required":True},
#     "GS06": {"id":"GS06", "type":"AN", "min":1, "max":9, "required":True},
#     "GS07": {"id":"GS07", "type":"ID", "min":1, "max":2, "required":True},
#     "GS08": {"id":"GS08", "type":"ID", "min":1, "max":12, "required":True},

#     # Transaction Set Header (ST)
#     "ST01": {"id":"ST01", "type":"ID", "min":3, "max":3, "required":True},
#     "ST02": {"id":"ST02", "type":"AN", "min":4, "max":9, "required":True},
#     "ST03": {"id":"ST03", "type":"AN", "min":1, "max":35, "required":True},

#     # Beginning Hierarchical Transaction (BHT)
#     "BHT01": {"id":"BHT01", "type":"ID", "min":4, "max":4, "required":True},
#     "BHT02": {"id":"BHT02", "type":"ID", "min":2, "max":2, "required":True},
#     "BHT03": {"id":"BHT03", "type":"AN", "min":1, "max":30, "required":True},
#     "BHT04": {"id":"BHT04", "type":"DT", "min":8, "max":8, "required":True},
#     "BHT05": {"id":"BHT05", "type":"TM", "min":4, "max":8, "required":True},
#     "BHT06": {"id":"BHT06", "type":"ID", "min":2, "max":2, "required":True},

#     # Hierarchical Level (HL)
#     "HL01": {"id":"HL01", "type":"AN", "min":1, "max":12, "required":True},
#     "HL02": {"id":"HL02", "type":"AN", "min":1, "max":12, "required":False},
#     "HL03": {"id":"HL03", "type":"ID", "min":1, "max":2, "required":True},
#     "HL04": {"id":"HL04", "type":"ID", "min":1, "max":1, "required":False},

#     # NM1 – Name
#     "NM101": {"id":"NM101", "type":"ID", "min":2, "max":2, "required":True},
#     "NM102": {"id":"NM102", "type":"ID", "min":1, "max":1, "required":True},
#     "NM103": {"id":"NM103", "type":"AN", "min":1, "max":60, "required":True},
#     "NM104": {"id":"NM104", "type":"AN", "min":1, "max":35, "required":False},
#     "NM105": {"id":"NM105", "type":"AN", "min":1, "max":35, "required":False},
#     "NM106": {"id":"NM106", "type":"AN", "min":1, "max":25, "required":False},
#     "NM107": {"id":"NM107", "type":"AN", "min":1, "max":25, "required":False},
#     "NM108": {"id":"NM108", "type":"ID", "min":1, "max":2, "required":False},
#     "NM109": {"id":"NM109", "type":"AN", "min":2, "max":80, "required":False},

#     # SBR – Subscriber Information
#     "SBR01": {"id":"SBR01", "type":"ID", "min":1, "max":1, "required":True},
#     "SBR02": {"id":"SBR02", "type":"AN", "min":1, "max":30, "required":False},

#     # PATIENT DETAIL
#     "PAT01": {"id":"PAT01", "type":"ID", "min":1, "max":1, "required":True},
#     "PAT02": {"id":"PAT02", "type":"AN", "min":1, "max":30, "required":False},

#     # Claim Information (CLM)
#     "CLM01": {"id":"CLM01", "type":"AN", "min":1, "max":20, "required":True},
#     "CLM02": {"id":"CLM02", "type":"R", "min":1, "max":18, "required":True},
#     "CLM03": {"id":"CLM03", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM04": {"id":"CLM04", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM05": {"id":"CLM05", "type":"AN", "min":1, "max":10, "required":False},
#     "CLM06": {"id":"CLM06", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM07": {"id":"CLM07", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM08": {"id":"CLM08", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM09": {"id":"CLM09", "type":"ID", "min":1, "max":2, "required":False},
#     "CLM10": {"id":"CLM10", "type":"ID", "min":1, "max":2, "required":False},

#     # Service Line (SV1)
#     "SV101": {"id":"SV101", "type":"AN", "min":1, "max":48, "required":True},
#     "SV102": {"id":"SV102", "type":"R", "min":1, "max":18, "required":True},
#     "SV103": {"id":"SV103", "type":"ID", "min":1, "max":2, "required":False},
#     "SV104": {"id":"SV104", "type":"N0", "min":1, "max":10, "required":True},
#     "SV105": {"id":"SV105", "type":"AN", "min":1, "max":2, "required":False},

#     # DTP – Date/Time Reference
#     "DTP01": {"id":"DTP01", "type":"ID", "min":3, "max":3, "required":True},
#     "DTP02": {"id":"DTP02", "type":"ID", "min":2, "max":3, "required":True},
#     "DTP03": {"id":"DTP03", "type":"DT", "min":8, "max":8, "required":True},

#     # REF – Reference Identification
#     "REF01": {"id":"REF01", "type":"ID", "min":2, "max":3, "required":True},
#     "REF02": {"id":"REF02", "type":"AN", "min":1, "max":50, "required":True},

#     # N3 – Address
#     "N301": {"id":"N301", "type":"AN", "min":1, "max":55, "required":True},
#     "N302": {"id":"N302", "type":"AN", "min":1, "max":55, "required":False},

#     # N4 – City/State/ZIP
#     "N401": {"id":"N401", "type":"AN", "min":2, "max":30, "required":True},
#     "N402": {"id":"N402", "type":"ID", "min":2, "max":2, "required":True},
#     "N403": {"id":"N403", "type":"AN", "min":3, "max":15, "required":True},

#     # HI – Diagnosis
#     "HI01": {"id":"HI01", "type":"AN", "min":1, "max":80, "required":True},
#     "HI02": {"id":"HI02", "type":"AN", "min":1, "max":80, "required":False},

#     # SE – Transaction Set Trailer
#     "SE01": {"id":"SE01", "type":"N0", "min":1, "max":10, "required":True},
#     "SE02": {"id":"SE02", "type":"AN", "min":4, "max":9, "required":True},

#     # GE – Functional Group Trailer
#     "GE01": {"id":"GE01", "type":"N0", "min":1, "max":6, "required":True},
#     "GE02": {"id":"GE02", "type":"AN", "min":1, "max":9, "required":True},

#     # IEA – Interchange Control Trailer
#     "IEA01": {"id":"IEA01", "type":"N0", "min":1, "max":5, "required":True},
#     "IEA02": {"id":"IEA02", "type":"AN", "min":9, "max":9, "required":True},

#     # PER — Submitter / Receiver Contact Info
#     "PER01": {"id": "PER01", "required": True, "max": 2, "type": "AN", "min": 2},
#     "PER02": {"id": "PER02", "required": True, "max": 80, "type": "AN"},
#     "PER03": {"id": "PER03", "required": False, "max": 2, "type": "AN"},
#     "PER04": {"id": "PER04", "required": False, "max": 80, "type": "AN"},
#     "PER05": {"id": "PER05", "required": False, "max": 2, "type": "AN"},
#     "PER06": {"id": "PER06", "required": False, "max": 80, "type": "AN"},
#     "PER07": {"id": "PER07", "required": False, "max": 2, "type": "AN"},
#     "PER08": {"id": "PER08", "required": False, "max": 80, "type": "AN"},

#     "PRV01": {"id": "PRV01", "required": True, "max": 2, "type": "AN"},
#     "PRV02": {"id": "PRV02", "required": False, "max": 80, "type": "AN"},
#     "PRV03": {"id": "PRV03", "required": False, "max": 1, "type": "AN"},
#     "PRV04": {"id": "PRV04", "required": False, "max": 2, "type": "AN"},
#     "PRV05": {"id": "PRV05", "required": False, "max": 80, "type": "AN"},

#     "N401": {"id": "N401", "required": True, "max": 30, "type": "AN"},  # City Name
#     "N402": {"id": "N402", "required": True, "max": 2, "type": "AN"},   # State Code
#     "N403": {"id": "N403", "required": True, "max": 15, "type": "AN"},  # ZIP Code
#     "N404": {"id": "N404", "required": False, "max": 10, "type": "AN"}, # ZIP Code Extension

#     "REF01": {"id": "REF01", "required": True, "max": 2, "type": "AN"},
#     "REF02": {"id": "REF02", "required": True, "max": 50, "type": "AN"},
#     "REF03": {"id": "REF03", "required": False, "max": 80, "type": "AN"},
#     "REF04": {"id": "REF04", "required": False, "max": 50, "type": "AN"},

#     "SBR01": {"id": "SBR01", "required": True, "max": 1, "type": "AN"},
#     "SBR02": {"id": "SBR02", "required": True, "max": 2, "type": "AN"},
#     "SBR03": {"id": "SBR03", "required": False, "max": 50, "type": "AN"},
#     "SBR04": {"id": "SBR04", "required": False, "max": 60, "type": "AN"},
#     "SBR05": {"id": "SBR05", "required": False, "max": 2, "type": "AN"},
#     "SBR06": {"id": "SBR06", "required": False, "max": 1, "type": "AN"},
#     "SBR08": {"id": "SBR08", "required": False, "max": 1, "type": "AN"},
#     "SBR09": {"id": "SBR09", "required": False, "max": 1, "type": "AN"},
#     "SBR10": {"id": "SBR10", "required": False, "max": 1, "type": "AN"},
# }




# x12_engine/registry/x837p/elements.py

ELEMENTS = {
    # ISA - Interchange Control Header
    "ISA01": {"id": "ISA01", "required": True, "max": 2, "type": "AN"},
    "ISA02": {"id": "ISA02", "required": True, "max": 10, "type": "AN"},
    "ISA03": {"id": "ISA03", "required": True, "max": 2, "type": "AN"},
    "ISA04": {"id": "ISA04", "required": True, "max": 10, "type": "AN"},
    "ISA05": {"id": "ISA05", "required": True, "max": 2, "type": "AN"},
    "ISA06": {"id": "ISA06", "required": True, "max": 15, "type": "AN"},
    "ISA07": {"id": "ISA07", "required": True, "max": 2, "type": "AN"},
    "ISA08": {"id": "ISA08", "required": True, "max": 15, "type": "AN"},
    "ISA09": {"id": "ISA09", "required": True, "max": 6, "type": "DT"},  # YYMMDD
    "ISA10": {"id": "ISA10", "required": True, "max": 4, "type": "TM"},  # HHMM
    "ISA11": {"id": "ISA11", "required": True, "max": 1, "type": "AN"},
    "ISA12": {"id": "ISA12", "required": True, "max": 5, "type": "AN"},
    "ISA13": {"id": "ISA13", "required": True, "max": 9, "type": "N"},
    "ISA14": {"id": "ISA14", "required": True, "max": 1, "type": "AN"},
    "ISA15": {"id": "ISA15", "required": True, "max": 1, "type": "AN"},
    "ISA16": {"id": "ISA16", "required": True, "max": 1, "type": "AN"},

    "IEA01": {"id": "IEA01", "required": True, "max": 5, "type": "N0"},   # Number of included functional groups
    "IEA02": {"id": "IEA02", "required": True, "max": 9, "type": "AN"},   # Interchange control number
    
    # --- Transaction Set Trailer ---
    "SE01": {"id": "SE01", "required": True, "max": 10, "type": "N0"},  # Number of included segments
    "SE02": {"id": "SE02", "required": True, "max": 4, "type": "AN"},   # ST control number

    "GE01": {"id": "GE01", "required": True, "max": 1, "type": "N0"},  # Number of transaction sets
    "GE02": {"id": "GE02", "required": True, "max": 9, "type": "AN"},  # Group control number

    # GS - Functional Group Header
    "GS01": {"id": "GS01", "required": True, "max": 2, "type": "AN"},
    "GS02": {"id": "GS02", "required": True, "max": 15, "type": "AN"},
    "GS03": {"id": "GS03", "required": True, "max": 15, "type": "AN"},
    "GS04": {"id": "GS04", "required": True, "max": 8, "type": "DT"},  # CCYYMMDD
    "GS05": {"id": "GS05", "required": True, "max": 8, "type": "TM"},  # HHMM
    "GS06": {"id": "GS06", "required": True, "max": 9, "type": "N"},
    "GS07": {"id": "GS07", "required": True, "max": 2, "type": "AN"},
    "GS08": {"id": "GS08", "required": True, "max": 12, "type": "AN"},

    # ST - Transaction Set Header
    "ST01": {"id": "ST01", "required": True, "max": 3, "type": "AN"},
    "ST02": {"id": "ST02", "required": True, "max": 9, "type": "AN"},
    "ST03": {"id": "ST03", "required": True, "max": 35, "type": "AN"},

    # NM1 - Name
    "NM101": {"id": "NM101", "required": True, "max": 2, "type": "AN"},
    "NM102": {"id": "NM102", "required": True, "max": 1, "type": "AN"},
    "NM103": {"id": "NM103", "required": False, "max": 60, "type": "AN"},
    "NM104": {"id": "NM104", "required": False, "max": 35, "type": "AN"},
    "NM105": {"id": "NM105", "required": False, "max": 35, "type": "AN"},
    "NM106": {"id": "NM106", "required": False, "max": 25, "type": "AN"},
    "NM107": {"id": "NM107", "required": False, "max": 2, "type": "AN"},
    "NM108": {"id": "NM108", "required": False, "max": 15, "type": "AN"},
    "NM109": {"id": "NM109", "required": False, "max": 20, "type": "AN"},

    # PER - Contact Info
    "PER01": {"id": "PER01", "required": True, "max": 2, "type": "AN"},
    "PER02": {"id": "PER02", "required": True, "max": 80, "type": "AN"},
    "PER03": {"id": "PER03", "required": False, "max": 2, "type": "AN"},
    "PER04": {"id": "PER04", "required": False, "max": 80, "type": "AN"},
    "PER05": {"id": "PER05", "required": False, "max": 2, "type": "AN"},
    "PER06": {"id": "PER06", "required": False, "max": 80, "type": "AN"},
    "PER07": {"id": "PER07", "required": False, "max": 2, "type": "AN"},
    "PER08": {"id": "PER08", "required": False, "max": 80, "type": "AN"},

    # N3 - Address
    "N301": {"id": "N301", "required": True, "max": 55, "type": "AN"},
    "N302": {"id": "N302", "required": False, "max": 55, "type": "AN"},

    # N4 - City/State/ZIP
    "N401": {"id": "N401", "required": True, "max": 30, "type": "AN"},
    "N402": {"id": "N402", "required": True, "max": 2, "type": "AN"},
    "N403": {"id": "N403", "required": True, "max": 15, "type": "AN"},
    "N404": {"id": "N404", "required": False, "max": 3, "type": "AN"},

    # DMG - Demographics
    "DMG01": {"id": "DMG01", "required": True, "max": 2, "type": "AN"},
    "DMG02": {"id": "DMG02", "required": True, "max": 8, "type": "DT"},
    "DMG03": {"id": "DMG03", "required": False, "max": 1, "type": "AN"},

    # CLM - Claim
    "CLM01": {"id": "CLM01", "required": True, "max": 20, "type": "AN"},
    "CLM02": {"id": "CLM02", "required": True, "max": 18, "type": "R"},
    "CLM03": {"id": "CLM03", "required": False, "max": 2, "type": "AN"},
    "CLM04": {"id": "CLM04", "required": False, "max": 2, "type": "AN"},
    "CLM05": {"id": "CLM05", "required": False, "max": 1, "type": "AN"},
    "CLM06": {"id": "CLM06", "required": False, "max": 1, "type": "AN"},
    "CLM07": {"id": "CLM07", "required": False, "max": 2, "type": "AN"},
    "CLM08": {"id": "CLM08", "required": False, "max": 2, "type": "AN"},
    "CLM09": {"id": "CLM09", "required": False, "max": 2, "type": "AN"},
    "CLM10": {"id": "CLM10", "required": False, "max": 3, "type": "AN"},

    # DTP - Date/Time Reference
    "DTP01": {"id": "DTP01", "required": True, "max": 3, "type": "AN"},
    "DTP02": {"id": "DTP02", "required": True, "max": 3, "type": "AN"},
    "DTP03": {"id": "DTP03", "required": True, "max": 35, "type": "AN"},

    # REF - Reference Identification
    "REF01": {"id": "REF01", "required": True, "max": 2, "type": "AN"},
    "REF02": {"id": "REF02", "required": True, "max": 50, "type": "AN"},
    "REF03": {"id": "REF03", "required": False, "max": 80, "type": "AN"},
    "REF04": {"id": "REF04", "required": False, "max": 50, "type": "AN"},

    # SBR - Subscriber Info
    "SBR01": {"id": "SBR01", "required": True, "max": 1, "type": "AN"},
    "SBR02": {"id": "SBR02", "required": True, "max": 2, "type": "AN"},
    "SBR03": {"id": "SBR03", "required": False, "max": 50, "type": "AN"},
    "SBR04": {"id": "SBR04", "required": False, "max": 60, "type": "AN"},
    "SBR05": {"id": "SBR05", "required": False, "max": 2, "type": "AN"},
    "SBR06": {"id": "SBR06", "required": False, "max": 1, "type": "AN"},
    "SBR07": {"id": "SBR07", "required": False, "max": 1, "type": "AN"},
    "SBR08": {"id": "SBR08", "required": False, "max": 1, "type": "AN"},
    "SBR09": {"id": "SBR09", "required": False, "max": 1, "type": "AN"},
    "SBR10": {"id": "SBR10", "required": False, "max": 1, "type": "AN"},

    # PRV - Provider Info
    "PRV01": {"id": "PRV01", "required": True, "max": 2, "type": "AN"},
    "PRV02": {"id": "PRV02", "required": False, "max": 2, "type": "AN"},
    "PRV03": {"id": "PRV03", "required": False, "max": 2, "type": "AN"},
    "PRV04": {"id": "PRV04", "required": False, "max": 1, "type": "AN"},
    "PRV05": {"id": "PRV05", "required": False, "max": 80, "type": "AN"},

    # HL - Hierarchical Level
    "HL01": {"id": "HL01", "required": True, "max": 12, "type": "AN"},
    "HL02": {"id": "HL02", "required": False, "max": 12, "type": "AN"},
    "HL03": {"id": "HL03", "required": True, "max": 2, "type": "AN"},
    "HL04": {"id": "HL04", "required": False, "max": 1, "type": "AN"},

    # LX - Service Line Counter
    "LX01": {"id": "LX01", "required": True, "max": 6, "type": "N"},

    # SV1 - Professional Service
    "SV101": {"id": "SV101", "required": True, "max": 48, "type": "AN"},
    "SV102": {"id": "SV102", "required": False, "max": 2, "type": "AN"},

    # SVD - Service Line Paid Amount
    "SVD01": {"id": "SVD01", "required": True, "max": 2, "type": "AN"},
    "SVD02": {"id": "SVD02", "required": True, "max": 10, "type": "R"},

    # CAS - Claim Adjustment
    "CAS01": {"id": "CAS01", "required": True, "max": 2, "type": "AN"},
    "CAS02": {"id": "CAS02", "required": True, "max": 10, "type": "R"},

    # Patient Information
    "PAT01": {"id": "PAT01", "required": False, "max": 2, "type": "AN"},
    "PAT02": {"id": "PAT02", "required": False, "max": 2, "type": "AN"},
    "PAT03": {"id": "PAT03", "required": False, "max": 1, "type": "AN"},
    "PAT04": {"id": "PAT04", "required": False, "max": 1, "type": "AN"},
    "PAT05": {"id": "PAT05", "required": False, "max": 2, "type": "AN"},

    # HI segment can have up to 12 elements (HI01–HI12), each representing a diagnosis code:
    "HI01": {"id": "HI01", "required": False, "max": 7, "type": "AN"},
    "HI02": {"id": "HI02", "required": False, "max": 7, "type": "AN"},
    "HI03": {"id": "HI03", "required": False, "max": 7, "type": "AN"},
    "HI04": {"id": "HI04", "required": False, "max": 7, "type": "AN"},
    "HI05": {"id": "HI05", "required": False, "max": 7, "type": "AN"},
    "HI06": {"id": "HI06", "required": False, "max": 7, "type": "AN"},
    "HI07": {"id": "HI07", "required": False, "max": 7, "type": "AN"},
    "HI08": {"id": "HI08", "required": False, "max": 7, "type": "AN"},
    "HI09": {"id": "HI09", "required": False, "max": 7, "type": "AN"},
    "HI10": {"id": "HI10", "required": False, "max": 7, "type": "AN"},
    "HI11": {"id": "HI11", "required": False, "max": 7, "type": "AN"},
    "HI12": {"id": "HI12", "required": False, "max": 7, "type": "AN"},

    # SV1 (Professional Service) segment reports line-item service details
    "SV101": {"id": "SV101", "required": True,  "max": 48, "type": "AN"},
    "SV102": {"id": "SV102", "required": True,  "max": 12, "type": "R"},
    "SV103": {"id": "SV103", "required": False, "max": 2,  "type": "AN"},
    "SV104": {"id": "SV104", "required": False, "max": 6,  "type": "R"},
    "SV105": {"id": "SV105", "required": False, "max": 2,  "type": "AN"},
    "SV106": {"id": "SV106", "required": False, "max": 2,  "type": "AN"},
    "SV107": {"id": "SV107", "required": False, "max": 10, "type": "AN"},
    "SV108": {"id": "SV108", "required": False, "max": 2,  "type": "AN"},
    "SV109": {"id": "SV109", "required": False, "max": 12, "type": "R"},

    # The SVD (Service Line Paid Amount) segment reports how much the payer paid for a service line
    "SVD01": {"id": "SVD01", "required": True,  "max": 48, "type": "AN"},
    "SVD02": {"id": "SVD02", "required": True,  "max": 12, "type": "R"},
    "SVD03": {"id": "SVD03", "required": True,  "max": 12, "type": "R"},
    "SVD04": {"id": "SVD04", "required": False, "max": 12, "type": "R"},
    "SVD05": {"id": "SVD05", "required": False, "max": 2,  "type": "AN"},
    "SVD06": {"id": "SVD06", "required": False, "max": 48, "type": "AN"},

    # The CAS (Claim Adjustment) segment provides details about any adjustments made to the claim amount
    # CAS is claim adjustment info, usually sent after each service line or at claim level.
    "CAS01": {"id": "CAS01", "required": True,  "max": 2,  "type": "AN"},
    "CAS02": {"id": "CAS02", "required": True,  "max": 2,  "type": "AN"},
    "CAS03": {"id": "CAS03", "required": True,  "max": 12, "type": "R"},
    "CAS04": {"id": "CAS04", "required": False, "max": 8,  "type": "R"},
    "CAS05": {"id": "CAS05", "required": False, "max": 2,  "type": "AN"},
    "CAS06": {"id": "CAS06", "required": False, "max": 2,  "type": "AN"},
    "CAS07": {"id": "CAS07", "required": False, "max": 12, "type": "R"},
    "CAS08": {"id": "CAS08", "required": False, "max": 8,  "type": "R"},
    "CAS09": {"id": "CAS09", "required": False, "max": 2,  "type": "AN"},
    "CAS10": {"id": "CAS10", "required": False, "max": 2,  "type": "AN"},
    "CAS11": {"id": "CAS11", "required": False, "max": 12, "type": "R"},
    "CAS12": {"id": "CAS12", "required": False, "max": 8,  "type": "R"},


    "AMT01": {"id": "AMT01", "required": True,  "max": 3,  "type": "AN"},
    "AMT02": {"id": "AMT02", "required": True,  "max": 12, "type": "R"},
    "AMT03": {"id": "AMT03", "required": False, "max": 1,  "type": "AN"},
    "AMT04": {"id": "AMT04", "required": False, "max": 3,  "type": "AN"},


    "K301": {"id": "K301", "required": True,  "max": 80, "type": "AN"},
    "K302": {"id": "K302", "required": False, "max": 80, "type": "AN"},
    "K303": {"id": "K303", "required": False, "max": 80, "type": "AN"},
    "K304": {"id": "K304", "required": False, "max": 80, "type": "AN"},
    "K305": {"id": "K305", "required": False, "max": 80, "type": "AN"},


    "NTE01": {"id": "NTE01", "required": False, "max": 3,  "type": "AN"},
    "NTE02": {"id": "NTE02", "required": True,  "max": 80, "type": "AN"},
    "NTE03": {"id": "NTE03", "required": False, "max": 80, "type": "AN"},
    "NTE04": {"id": "NTE04", "required": False, "max": 80, "type": "AN"},

}
