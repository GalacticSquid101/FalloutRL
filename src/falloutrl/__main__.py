"""The main script executable of the roguelike"""

import tcod

from falloutrl.engine import Engine


def main() -> None:
    """The main function of the program."""
    screen_width = 120
    screen_height = 80

    tileset = tcod.tileset.load_tilesheet(
        "./src/falloutrl/data/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    Engine(screen_width, screen_height, tileset).run()


if __name__ == "__main__":
    main()
