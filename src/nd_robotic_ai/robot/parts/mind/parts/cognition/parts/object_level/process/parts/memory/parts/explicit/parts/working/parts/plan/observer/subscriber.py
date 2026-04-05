from abc import abstractmethod, ABC

from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.plan import \
    Plan as CurrentWorkingMemoryPlan


class Subscriber(ABC):

    @abstractmethod
    def handle_updated_plan(self, plan: CurrentWorkingMemoryPlan):
        pass
