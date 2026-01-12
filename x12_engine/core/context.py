from datetime import datetime

class X12Context:
    """Context for control numbers and envelope data"""
    def __init__(self):
        self.isa_control = 1
        self.gs_control = 1
        self.st_control = 1

    def next_isa(self):
        val = self.isa_control
        self.isa_control += 1
        return str(val).zfill(9)

    def next_gs(self):
        val = self.gs_control
        self.gs_control += 1
        return str(val)

    def next_st(self):
        val = self.st_control
        self.st_control += 1
        return str(val).zfill(4)

    def date(self):
        return datetime.now().strftime("%y%m%d")

    def time(self):
        return datetime.now().strftime("%H%M")
