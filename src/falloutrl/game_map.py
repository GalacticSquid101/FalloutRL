"""Implements the GameMaps that make up the world."""

import numpy as np
from tcod.console import Console

from falloutrl.procgen.rectangular_room import RectangularRoom
from falloutrl.tiles import floor, wall


class GameMap:
    """Holds all relevant information for the GameMap"""

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height

        self.tiles = np.full((width, height), fill_value=wall, order="F")

        self.tiles[RectangularRoom(10, 10, 20, 30).inner] = floor

    def render(self, console: Console) -> None:
        """Renders the game map."""
        console.rgb[0 : self.width, 0 : self.height] = self.tiles["light"]
