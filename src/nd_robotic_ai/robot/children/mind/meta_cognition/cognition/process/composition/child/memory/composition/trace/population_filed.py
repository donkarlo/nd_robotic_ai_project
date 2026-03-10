from nd_robotic_ai.structure.kind.body.nervous.neuron.collection.population_activity_field import PopulationActivityField
from typing import Any

from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.trace.trace import Trace


class PopulationField(Trace):
    def __init__(self, formatted_data:Any, time:float, kind:int):
        """
        time and role are already determined by a population of activity field from example by ROS
        Args:
            formatted_data: 
            time: 
            kind:
        """
        self._formatted_data = formatted_data
        self._time = time
        self._kind = kind

    def get_formatted_data(self) -> Any:
        return self._formatted_data

    def get_time(self) -> float:
        return self._time

    def get_kind(self) -> int:
        return self._kind

    def convert_to_population_acrtivity_field(self, decoder)->PopulationActivityField:
        pass

    def set_time(self, time:float) -> None:
        self._time = time

    def set_type(self, kind:int) -> None:
        self._kind = kind

    def set_formatted_data(self, formatted_data:Any) -> None:
        self._formatted_data = formatted_data