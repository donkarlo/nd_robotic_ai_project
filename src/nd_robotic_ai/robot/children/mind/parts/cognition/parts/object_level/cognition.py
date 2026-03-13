from nd_robotic_ai.robot.children.mind.parts.cognition.parts.object_level.process.process import Process
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit

class Cognition(RobotCompositeUnit):
    """
    -  the processing part of the mind
    - Bridge between language and ontology by decision making and acting
    - 
    """
    def __init__(self):
        RobotCompositeUnit.__init__(self)
        self.add_child(Process())