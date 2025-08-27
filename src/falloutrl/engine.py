"""Implements the game engine."""

from __future__ import annotations

import tcod

from falloutrl import color
from falloutrl.game_map import GameMap
from falloutrl.ui.message_log import MessageLog

background_image = tcod.image.load("./src/falloutrl/data/background.png")[:, :, :3]
pipboy_background_image = tcod.image.load("./src/falloutrl/data/pipboy_background.png")[
    :, :, :3
]


class Engine:
    """The game engine that drives the game."""

    def __init__(
        self, screen_width: int, screen_height: int, tileset: tcod.tileset.Tileset
    ):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.tileset = tileset
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.top_bar_width = screen_width
        self.top_bar_height = 15
        self.log_width = 25
        self.log_height = screen_height - self.top_bar_height
        self.map_width = screen_width - self.log_width
        self.map_height = screen_height - self.top_bar_height
        self.pipboy_width = screen_width // 2
        self.pipboy_height = screen_height // 2
        self._root_console = tcod.console.Console(screen_width, screen_height, "F")
        self._top_bar_console = tcod.console.Console(
            self.top_bar_width, self.top_bar_height, "F"
        )
        self._log_console = tcod.console.Console(self.log_width, self.log_height, "F")
        self._map_console = tcod.console.Console(self.map_width, self.map_height, "F")
        self.game_map = GameMap(self.map_width, self.map_height)
        self._pipboy_console = tcod.console.Console(
            self.pipboy_width, self.pipboy_height, "F"
        )
        self.pipboy_shown = False

    def run(self) -> None:
        """Loops infinitely controlling the game loop."""
        with tcod.context.new(
            columns=self.screen_width,
            rows=self.screen_height,
            tileset=self.tileset,
            title="FalloutRL",
        ) as context:
            while True:
                self.render()
                context.present(self._root_console)
                for event in tcod.event.wait():
                    context.convert_event(event)
                    if isinstance(event, tcod.event.Quit):
                        raise SystemExit()
                    if (
                        isinstance(event, tcod.event.KeyDown)
                        and event.sym == tcod.event.KeySym.I
                    ):
                        self.pipboy_shown = True

                self.message_log.add_message("Run Loop!")

    def render(self) -> None:
        """Render the whole game here"""
        self._root_console.clear()

        # self._root_console.draw_semigraphics(background_image)

        self._top_bar_console.print(
            1, 1, text="UI CONSOLE", fg=color.UI_FG, bg=color.UI_BG
        )
        self._top_bar_console.blit(self._root_console, bg_alpha=0.5)

        self.message_log.render(
            self._log_console, 0, 0, self.log_width, self.log_height
        )
        self._log_console.blit(
            self._root_console,
            self.screen_width - self.log_width,
            self.screen_height - self.log_height,
            bg_alpha=0.5,
        )

        self.game_map.render(self._map_console)
        self._map_console.blit(self._root_console, 0, self.top_bar_height, bg_alpha=0.5)

        if self.pipboy_shown:
            self._pipboy_console.draw_semigraphics(background_image)
            self._pipboy_console.draw_frame(0, 0, self.pipboy_width, self.pipboy_height)
            self._pipboy_console.print(
                0,
                0,
                text="PIPBOY 3000",
                width=self.pipboy_width,
                height=1,
                fg=color.UI_FG,
                bg=color.UI_BG,
                alignment=tcod.constants.CENTER,
            )
            self._pipboy_console.blit(
                self._root_console,
                (self.screen_width - self.pipboy_width) // 2,
                (self.screen_height - self.pipboy_height) // 2,
            )
