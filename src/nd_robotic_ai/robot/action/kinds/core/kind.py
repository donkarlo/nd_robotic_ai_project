from __future__ import annotations

from dataclasses import dataclass
from typing import List

from nd_robotic_ai.robot.action.kinds.children import Child


@dataclass(frozen=True)
class Kind:
    title: str
    children: List[Child]
