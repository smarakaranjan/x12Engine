from x12_engine.errors import LoopRepeatExceeded

class Loop:
    def __init__(self, loop_id, children, max_repeat=1, required=False):
        self.loop_id = loop_id
        self.children = children  # list of Segment or Loop
        self.max_repeat = max_repeat
        self.required = required

    def render(self, data_list, writer):
        if not data_list:
            if self.required:
                raise LoopRepeatExceeded(f"{self.loop_id} is required")
            return
        if not isinstance(data_list, list):
            data_list = [data_list]
        if len(data_list) > self.max_repeat:
            raise LoopRepeatExceeded(f"{self.loop_id} exceeded repeat limit")
        for data in data_list:
            for child in self.children:
                if hasattr(child, "segment_id"):
                    writer.write(child.render(data))
                else:
                    child.render(data.get(child.loop_id), writer)
