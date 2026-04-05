from nd_robotic_ai.robot.composition.composite import Composite as RobotComposite
from nd_robotic_ai.robot.parts.body.body import Body
from nd_robotic_ai.robot.parts.mind.mind import Mind
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.parts.plan.plan import \
    Plan as WorkingMemoryPlan
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.memory.parts.explicit.parts.working.working import \
    Working
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.thinking.parts.planning.planning import \
    Planning
from nd_utility.os.file_system.directory.directory import Directory

class Robot(RobotComposite):
    """
    A robot is a singletone that is acceptable for comunication therough the structure
    Each robot is an intersection between mind and body, it relates a Train of ActionPotential Train (NeuralCoding) to a trace society formatted data
    """

    def __init__(self):
        """
        dont assign a title in args, a born baby doent know its title
        Args:
            structure:
        """
        RobotComposite.__init__(self)


        self.add_child(Body())
        self.add_child(Mind())



    def run(self) -> None:
        # All goals must be attached to this one so that teh robot decides the priority between them
        working_memory_plan = self.get_child(Working).get_child(WorkingMemoryPlan)
        working_memory_plan.run()
