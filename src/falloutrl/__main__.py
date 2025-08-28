"""The main script executable of the roguelike"""

import tcod

from falloutrl.engine import Engine
from falloutrl.input_handlers.event_handler import EventHandler


def main() -> None:
    """The main function of the program."""
    screen_width = 120
    screen_height = 80

    tileset = tcod.tileset.load_tilesheet(
        "./src/falloutrl/data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    Engine(screen_width, screen_height, tileset).run()

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


if __name__ == "__main__":
    main()
