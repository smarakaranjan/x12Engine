class X12Writer:
    """Buffer for X12 segments"""
    def __init__(self):
        self._buffer = []

    def write(self, segment_str):
        self._buffer.append(segment_str)

    def render(self):
        return "\n".join(self._buffer)
