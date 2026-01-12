from x12_engine.errors import X12Error

class RequiredIf:
    def __init__(self, field, condition):
        self.field = field
        self.condition = condition

    def validate(self, payload):
        if self.condition(payload) and self.field not in payload:
            raise X12Error(f"{self.field} is required by condition")
