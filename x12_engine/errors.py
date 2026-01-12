# x12_engine/errors.py

class X12Error(Exception):
    """Base class for all X12 engine exceptions."""
    def __init__(self, message="", segment=None, element=None):
        super().__init__(message)
        self.segment = segment
        self.element = element

    def __str__(self):
        context = []
        if self.segment:
            context.append(f"Segment: {self.segment}")
        if self.element:
            context.append(f"Element: {self.element}")
        ctx_str = " | ".join(context)
        return f"{super().__str__()} {ctx_str}" if ctx_str else super().__str__()


class RequiredElementMissing(X12Error):
    """Raised when a required element is missing."""
    def __init__(self, segment=None, element=None):
        msg = f"Required element missing."
        super().__init__(msg, segment, element)


class InvalidElementType(X12Error):
    """Raised when element value does not match expected type."""
    def __init__(self, segment=None, element=None, value=None, expected_type=None):
        msg = f"Invalid element type. Expected {expected_type}, got value '{value}'."
        super().__init__(msg, segment, element)


class ElementOverflow(X12Error):
    """Raised when element value exceeds maximum length."""
    def __init__(self, segment=None, element=None, value=None, max_len=None):
        msg = f"Element value '{value}' exceeds max length {max_len}."
        super().__init__(msg, segment, element)


class ElementUnderflow(X12Error):
    """Raised when element value is shorter than minimum length."""
    def __init__(self, segment=None, element=None, value=None, min_len=None):
        msg = f"Element value '{value}' shorter than min length {min_len}."
        super().__init__(msg, segment, element)


class LoopRepeatExceeded(X12Error):
    """Raised when loop repeats more than allowed."""
    def __init__(self, loop_id=None, max_repeat=None):
        msg = f"Loop '{loop_id}' exceeded max repeat of {max_repeat}."
        super().__init__(msg, segment=loop_id)


class ControlMismatch(X12Error):
    """Raised when control numbers do not match (SE/GE/IEA)."""
    def __init__(self, control_type=None, expected=None, actual=None):
        msg = f"Control mismatch for {control_type}: expected {expected}, got {actual}."
        super().__init__(msg)
