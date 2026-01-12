from x12_engine.errors import LoopRepeatExceeded, X12Error

class StructuralValidator:
    def validate_loop(self, loop, data):
        if not data:
            if loop.required:
                raise LoopRepeatExceeded(f"{loop.loop_id} missing")
            return
        if not isinstance(data, list):
            data = [data]
        if len(data) > loop.max_repeat:
            raise LoopRepeatExceeded(f"{loop.loop_id} repeat exceeded")
        for item in data:
            for child in loop.children:
                if hasattr(child, "segment_id"):
                    if child.spec.get("required") and child.segment_id not in item:
                        raise X12Error(f"{child.segment_id} missing")
                else:
                    self.validate_loop(child, item.get(child.loop_id))
