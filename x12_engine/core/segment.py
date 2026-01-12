class Segment:
    def __init__(self, segment_id, elements):
        self.segment_id = segment_id
        self.elements = elements  # list of Element objects

    def render(self, values, sep="*"):
        parts = [self.segment_id]
        for el in self.elements:
            parts.append(el.render(values.get(el.spec["id"])))
        return sep.join(parts)
