from __future__ import annotations

from dataclasses import dataclass
from typing import List

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.long_term.parts.semantic.parts.action.kinds.children import Child


@dataclass(frozen=True)
class Kind:
    title: str
    children: List[Child]
