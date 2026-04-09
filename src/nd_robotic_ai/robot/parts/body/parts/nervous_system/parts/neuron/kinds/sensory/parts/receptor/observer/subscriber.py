from abc import ABC, abstractmethod

from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.neuron.kinds.sensory.parts.receptor.observation.observation import \
    Observation


class Subscriber(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def handle_new_observation(self, new_observation:Observation) -> None:
        ...
