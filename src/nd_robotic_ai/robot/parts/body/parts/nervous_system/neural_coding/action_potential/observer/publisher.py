from abc import ABC, abstractmethod

from nd_math.probability.bayesian.observation import Observation


class Publisher(ABC):
    @abstractmethod
    def fire_action_potential(self, observation:Observation) -> None:
        ...
