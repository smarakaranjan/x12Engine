from x12_engine.core.loop import Loop
from .segments import create_segment

LOOPS = {
    # 1000A – Submitter Name
    "1000A": Loop(
        "1000A",
        [
            create_segment("NM1"),  # Submitter Name
            create_segment("PER"),  # Submitter Contact
        ],
        max_repeat=1,
        required=True,
    ),

    # 1000B – Receiver Name
    "1000B": Loop(
        "1000B",
        [
            create_segment("NM1"),  # Receiver Name
        ],
        max_repeat=1,
        required=True,
    ),

    # 2000A – Billing Provider Hierarchical Level
    "2000A": Loop(
        "2000A",
        [
            create_segment("HL"),   # Provider HL
            create_segment("PRV"),  # Provider Specialty
            create_segment("NM1"),   # Billing Provider Name
            create_segment("N3"),    # Address
            create_segment("N4"),    # City/State/ZIP
            create_segment("REF"),   # Tax ID / Other ID
            create_segment("PER"),   # Contact Info
        ],
        max_repeat=1,
        required=True,
    ),

    # 2000B – Subscriber Hierarchical Level
    "2000B": Loop(
        "2000B",
        [
            create_segment("HL"),  # Subscriber HL
            create_segment("SBR"), # Subscriber Info
            create_segment("NM1"), # Subscriber Name
            create_segment("N3"),  # Address
            create_segment("N4"),  # City/State/ZIP
            create_segment("DMG"), # Demographics
        ],
        max_repeat=100,  # Can repeat per subscriber
        required=True,
    ),

    # 2010BA – Subscriber Name/Address
    "2010BA": Loop(
        "2010BA",
        [
            create_segment("NM1"),  # Subscriber Name
            create_segment("N3"),   # Address
            create_segment("N4"),   # City/State/ZIP
            create_segment("REF"),  # Subscriber ID / Policy Number
        ],
        max_repeat=1,
        required=True,
    ),

    # 2000C – Patient Hierarchical Level
    "2000C": Loop(
        "2000C",
        [
            create_segment("HL"),  # Patient HL
            create_segment("PAT"), # Patient Info
        ],
        max_repeat=100,
        required=True,
    ),

    # 2010CA – Patient Name/Address
    "2010CA": Loop(
        "2010CA",
        [
            create_segment("NM1"),  # Patient Name
            create_segment("N3"),   # Address
            create_segment("N4"),   # City/State/ZIP
            create_segment("DMG"),  # Demographics
            create_segment("REF"),  # Patient ID
        ],
        max_repeat=1,
        required=True,
    ),

    # 2300 – Claim Information Loop
    "2300": Loop(
        "2300",
        [
            create_segment("CLM"),   # Claim Info
            create_segment("DTP"),   # Service Dates
            create_segment("REF"),   # Other claim references
            create_segment("HI"),    # Diagnosis Codes
            create_segment("LX"),    # Service Line Counter
            create_segment("SV1"),   # Professional Service
            create_segment("SVD"),   # Payer Paid Info
            create_segment("CAS"),   # Adjustments
            create_segment("AMT"),   # Amounts
            create_segment("K3"),    # File Notes
            create_segment("NTE"),   # Claim Note
        ],
        max_repeat=100,
        required=True,
    ),

    # 2400 – Service Line
    "2400": Loop(
        "2400",
        [
            create_segment("LX"),    # Service Line Counter
            create_segment("SV1"),   # Professional Service
            create_segment("DTP"),   # Service Dates
            create_segment("REF"),   # Line Info
            create_segment("CAS"),   # Adjustments
            create_segment("SVD"),   # Payer Paid Info
            create_segment("AMT"),   # Amounts
            create_segment("K3"),    # File Notes
            create_segment("NTE"),   # Service Line Note
        ],
        max_repeat=9999,  # Service lines can repeat per claim
        required=True,
    ),

    # 2000D – Dependent (if any)
    "2000D": Loop(
        "2000D",
        [
            create_segment("HL"),
            create_segment("PAT"),
        ],
        max_repeat=100,
        required=False,
    ),

    # 1000C – Payer Name
    "1000C": Loop(
        "1000C",
        [
            create_segment("NM1"),
            create_segment("N3"),
            create_segment("N4"),
        ],
        max_repeat=1,
        required=True,
    ),
}
