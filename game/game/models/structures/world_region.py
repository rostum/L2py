from __future__ import annotations

import typing
from dataclasses import dataclass, field

from common.dataclass import BaseDataclass
from common.helpers.cython import cython

# import game.models.structures.object.object


@dataclass
class WorldRegion(BaseDataclass):
    playable_objects: typing.List["L2Object"]
    visible_objects: typing.List["game.models.structures.object.object.L2Object"]
    neighbours: typing.List["WorldRegion"]
    tile_x: cython.long
    tile_y: cython.long
    active: cython.bint
    zone_manager: None


WorldRegion.update_forward_refs(
    # **{"game.models.structures.object.object.L2Object": game.models.structures.object.object.L2Object}
)
