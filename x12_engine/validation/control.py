from x12_engine.errors import ControlMismatch

class ControlValidator:
    def validate_se(self, se01, count):
        if int(se01) != count:
            raise ControlMismatch("SE segment count mismatch")

    def validate_ge(self, ge01, st_count):
        if int(ge01) != st_count:
            raise ControlMismatch("GE ST count mismatch")

    def validate_iea(self, iea01, gs_count):
        if int(iea01) != gs_count:
            raise ControlMismatch("IEA GS count mismatch")
