from x12_engine.core.segment import Segment
from .elements import ELEMENTS
from x12_engine.core.element import Element

# -------------------------------
# Segment Definitions
# Each segment references its elements by ID
# Ordered according to X12 837P standard
# -------------------------------
SEGMENTS = {
    # Interchange Control Header
    "ISA": [
        "ISA01","ISA02","ISA03","ISA04","ISA05","ISA06",
        "ISA07","ISA08","ISA09","ISA10","ISA11","ISA12",
        "ISA13","ISA14","ISA15","ISA16"
    ],

    # Functional Group Header
    "GS": ["GS01","GS02","GS03","GS04","GS05","GS06","GS07","GS08"],

    # Transaction Set Header
    "ST": ["ST01","ST02","ST03"],

    # Beginning Hierarchical Transaction
    "BHT": ["BHT01","BHT02","BHT03","BHT04","BHT05","BHT06"],

    # Hierarchical Level
    "HL": ["HL01","HL02","HL03","HL04"],

    # Name segments
    "NM1": ["NM101","NM102","NM103","NM104","NM105","NM106","NM107","NM108","NM109"],
    "PER": ["PER01","PER02","PER03","PER04","PER05","PER06","PER07","PER08"],

    # Claim Information
    "CLM": ["CLM01","CLM02","CLM03","CLM04","CLM05","CLM06","CLM07","CLM08","CLM09","CLM10"],

    # Subscriber Info
    "SBR": ["SBR01","SBR02","SBR03","SBR04","SBR05","SBR06","SBR07","SBR08"],

    # Patient Info
    "PAT": ["PAT01","PAT02"],

    # Address
    "N3": ["N301","N302"],
    "N4": ["N401","N402","N403","N404"],

    # Demographics
    "DMG": ["DMG01","DMG02","DMG03"],

    # Date/Time
    "DTP": ["DTP01","DTP02","DTP03"],

    # Service Line
    "LX": ["LX01"],
    "SV1": ["SV101","SV102","SV103","SV104","SV105"],
    "SVD": ["SVD01","SVD02","SVD03","SVD04","SVD05","SVD06"],

    # Adjustments
    "CAS": ["CAS01","CAS02","CAS03","CAS04","CAS05","CAS06","CAS07","CAS08"],

    # File Notes / Claim Notes
    "K3": ["K301","K302","K303", "K304", "K305"],
    "NTE": ["NTE01","NTE02","NTE03", "NTE04"],

    # Reference Identification
    "REF": ["REF01","REF02","REF03","REF04"],

    # Diagnosis
    "HI": ["HI01","HI02","HI03","HI04","HI05","HI06","HI07","HI08","HI09","HI10"],

    # Transaction Set Trailer
    "SE": ["SE01","SE02"],
    

    # Functional Group Trailer
    "GE": ["GE01","GE02"],

    # Interchange Control Trailer
    "IEA": ["IEA01","IEA02"],

    "PRV": ["PRV01", "PRV02", "PRV03", "PRV04", "PRV05"],  # adjust elements as per X12 837P standard
    
    "AMT": ["AMT01", "AMT02", "AMT03", "AMT04"]


    
    
}

# -------------------------------
# Segment Factory
# -------------------------------
def create_segment(seg_id):
    """
    Factory function to create a Segment instance with its Elements.
    Validates that each element exists in ELEMENTS dictionary.
    """
    if seg_id not in SEGMENTS:
        raise ValueError(f"Unknown segment id: {seg_id}")

    elements = []
    for e_id in SEGMENTS[seg_id]:
        if e_id not in ELEMENTS:
            raise ValueError(f"Segment '{seg_id}' references unknown element '{e_id}'")
        elements.append(Element(ELEMENTS[e_id]))

    return Segment(seg_id, elements)
