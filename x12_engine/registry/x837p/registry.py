from .segments import create_segment
from .loops import LOOPS

class X837PRegistry:
    def segment(self, seg_id):
        return create_segment(seg_id)

    def loop(self, loop_id):
        return LOOPS[loop_id]
