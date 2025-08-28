"""Implements the creation of tiles"""

import numpy as np

from falloutrl import color

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphic_dt),
        ("light", graphic_dt),
    ]
)


def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: tuple[int, tuple[int, int, int], tuple[int, int, int]],
    light: tuple[int, tuple[int, int, int], tuple[int, int, int]],
) -> np.ndarray:
    """Helper funciton for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


SHROUD = np.array((ord(" "), color.WHITE, color.BLACK), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), color.WHITE, color.WASTELAND_FLOOR_DARK),
    light=(ord(" "), color.WHITE, color.WASTELAND_FLOOR_LIGHT),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), color.WHITE, color.WASTELAND_WALL_DARK),
    light=(ord(" "), color.WHITE, color.WASTELAND_WALL_LIGHT),
)
