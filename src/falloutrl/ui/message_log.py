"""Implements MessageLog and Messages."""

import textwrap
from typing import Iterable, Reversible

import tcod

from falloutrl import color


class Message:
    """The base message type"""

    def __init__(self, text: str, fg: tuple[int, int, int]):
        self.plain_text = text
        self.fg = fg
        self.count = 1

    @property
    def full_text(self) -> str:
        """The full text of this message, including the count if necessary"""
        if self.count > 1:
            return f"{self.plain_text} (x{self.count})"
        return self.plain_text


class MessageLog:
    """The log that contains messages"""

    def __init__(self) -> None:
        self.messages: list[Message] = []

    def add_message(
        self,
        text: str,
        fg: tuple[int, int, int] = color.UI_FG,
        *,
        stack: bool = True,
    ) -> None:
        """Adds a message to the log"""
        if stack and self.messages and text == self.messages[-1].plain_text:
            self.messages[-1].count += 1
        else:
            self.messages.append(Message(text, fg))

    def render(
        self,
        console: tcod.console.Console,
        x: int,
        y: int,
        width: int,
        height: int,
    ) -> None:
        """Render this log over the given area"""
        console.draw_frame(
            x, y, width=width, height=height, fg=color.UI_FG, bg=color.UI_BG
        )
        console.print(
            x,
            y,
            text="Message Log",
            width=width,
            height=1,
            fg=color.UI_FG,
            bg=color.UI_BG,
            alignment=tcod.constants.CENTER,
        )
        self.render_messages(
            console, x + 1, y + 1, width - 2, height - 2, self.messages
        )

    @staticmethod
    def wrap(string: str, width: int) -> Iterable[str]:
        """Return a wrapped text message."""
        for line in string.splitlines():
            yield from textwrap.wrap(line, width, expand_tabs=True)

    @classmethod
    def render_messages(
        cls,
        console: tcod.console.Console,
        x: int,
        y: int,
        width: int,
        height: int,
        messages: Reversible[Message],
    ) -> None:
        """Render the messages provided."""
        y_offset = height - 1

        for message in reversed(messages):
            for line in reversed(list(cls.wrap(message.full_text, width))):
                console.print(x=x, y=y + y_offset, text=line, fg=message.fg)
                y_offset -= 1
                if y_offset < 0:
                    return
