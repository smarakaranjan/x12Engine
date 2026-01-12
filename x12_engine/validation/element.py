from x12_engine.errors import ElementValidationError

class ElementValidator:
    def validate_segment(self, segment, values):
        for el in segment.elements:
            el.render(values.get(el.spec["id"]))
