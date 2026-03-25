from abc import ABC

from nd_robotic_ai.robot.parts.body.body import Body
from nd_robotic_ai.robot.parts.mind.mind import Mind
from nd_robotic_ai.robot.goal.composite.component import Component as ComponentGoal
from nd_robotic_ai.robot.goal.composite.composite import Composite as CompositeGoal
from nd_utility.os.file_system.directory.directory import Directory
# from nd_robotic_ai.robot.classification.classification.mind.object_level.process.classification.thinking.decision_making.planning.planning import \
#     Planning

from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent



class Robot(RobotCompositeComponent):
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
        RobotCompositeComponent.__init__(self)

        self._composite_goal = None
        self._composite_action = None

        self.add_child(Body())
        self.add_child(Mind())



    @classmethod
    def init_from_directory(cls, os_directory: Directory):
        # TODO: To be completed
        return cls(os_directory)

    def attach_goal(self, parent_goal: CompositeGoal, goal: ComponentGoal) -> None:
        """
        We can just attach goals and not actions. Planning in mind>process>thinking>decision making  makes a classification action
        Args:
            parent_goal:
            goal:

        Returns:

        """
        self._composite_goal.get_child(parent_goal).add_child(goal)


    def run(self):
        # All goals must be attached to this one so that teh robot decides the priority between them
        # suprise_poise_goal = SurprisePoise()
        #
        # self._composite_goal = CompositeGoal(suprise_poise_goal, None)
        # planner = Planning(self._composite_goal)
        # self._composite_action = planner.get_composite_action()
        #
        # self._composite_action.run()
        ...

    def add_even_specific_knowledge(self)->None:
        pass
