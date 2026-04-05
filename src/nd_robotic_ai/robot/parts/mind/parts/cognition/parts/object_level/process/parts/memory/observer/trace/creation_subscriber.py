from abc import ABC, abstractmethod

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.leaf.leaf import \
    Trace


class CreationSubscriber(ABC):
    @abstractmethod
    def handle_created_trace(self, trace: Trace) -> None: ...
