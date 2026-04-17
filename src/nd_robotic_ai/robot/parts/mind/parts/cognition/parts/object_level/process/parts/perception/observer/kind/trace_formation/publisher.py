from abc import ABC, abstractmethod

from nd_math.probability.bayesian.observation import Observation
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.observer.kind.trace_formation.subscriber import \
    Subscriber as PerceptionSubscriber


class Publisher(ABC):
    @abstractmethod
    def publish_trace_formation(self, observation: Observation) -> None:
        ...

    @abstractmethod
    def attach_subcriber(self, subscriber: PerceptionSubscriber) -> None:
        ...

    @abstractmethod
    def notify_subscribers(self) -> None:
        ...
