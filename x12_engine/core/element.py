from x12_engine.errors import *

class Element:
    def __init__(self, spec):
        self.spec = spec  # dict: {id, required, max, type}

    def render(self, value):
        if value is None or value == "":
            if self.spec.get("required"):
                raise RequiredElementMissing(f"{self.spec['id']} is required")
            return ""
        value = str(value)
        max_len = self.spec.get("max")
        if max_len and len(value) > max_len:
            raise ElementOverflow(f"{self.spec['id']} exceeded max length")
        return value
