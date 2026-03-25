from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.composition.component import \
    Component as MemoryComponent
from typing import List

from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def __init__(self, source_memory_component: MemoryComponent):
        ...

    @abstractmethod
    def segregate(self)->None:
        ...

    @abstractmethod
    def get_segregated_components(self)->List[MemoryComponent]:
        ...