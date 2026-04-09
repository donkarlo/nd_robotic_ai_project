from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.plan import \
    Plan as CurrentWorkingMemoryPlan


class Publisher:
    def __init__(self):
        self._subscribers = []

    def notify(self, current_working_plan: CurrentWorkingMemoryPlan):
        for subscriber in self._subscribers:
            subscriber.notify(current_working_plan)
