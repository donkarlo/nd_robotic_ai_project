from abc import ABC, abstractmethod

from nd_math.probability.bayesian.observation import Observation


class Publisher(ABC):
    @abstractmethod
    def publish_new_observation(self, observation:Observation) -> None:
        ...
