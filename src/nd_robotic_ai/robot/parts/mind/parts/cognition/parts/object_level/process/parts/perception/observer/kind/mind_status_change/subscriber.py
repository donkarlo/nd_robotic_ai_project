from abc import ABC, abstractmethod
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.trace.trace import Trace


class Subscriber(ABC):

    @abstractmethod
    def handle_new_formed_trace(self, trace:Trace) -> None:
        ...
