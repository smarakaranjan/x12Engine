class Registry:
    """Base registry to fetch segments/loops/elements by ID"""
    def __init__(self, segments, loops, elements):
        self._segments = segments
        self._loops = loops
        self._elements = elements

    def segment(self, seg_id):
        from x12_engine.core.segment import Segment
        from x12_engine.core.element import Element
        from x12_engine.registry.x837p.segments import SEGMENTS, ELEMENTS

        if seg_id not in SEGMENTS:
            raise ValueError(f"Unknown segment {seg_id}")
        elems = [Element(ELEMENTS[e]) for e in SEGMENTS[seg_id]]
        return Segment(seg_id, elems)

    def loop(self, loop_id):
        if loop_id not in self._loops:
            raise ValueError(f"Unknown loop {loop_id}")
        return self._loops[loop_id]

    def element(self, el_id):
        if el_id not in self._elements:
            raise ValueError(f"Unknown element {el_id}")
        return self._elements[el_id]
