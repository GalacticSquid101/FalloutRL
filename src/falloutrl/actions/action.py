"""Implements the base action."""

import auto_all  # type: ignore[import-untyped]

auto_all.start_all()


class Action:
    pass


class EscapeAction(Action):
    pass


class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy


auto_all.end_all()
