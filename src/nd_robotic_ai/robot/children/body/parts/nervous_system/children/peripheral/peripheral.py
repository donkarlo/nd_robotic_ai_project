from nd_robotic_ai.robot.children.body.parts.nervous_system.children.peripheral.children.autonomic.autonomic import Autonomic
from nd_robotic_ai.robot.children.body.parts.nervous_system.children.peripheral.children.enteric.enteric import Enteric
from nd_robotic_ai.robot.children.body.parts.nervous_system.children.peripheral.children.somatic.somatic import Somatic
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit


class Peripheral(RobotCompositeUnit):
    def __init__(self):
        RobotCompositeUnit.__init__(self)
        self.add_child(Somatic())
        self.add_child(Enteric())
        self.add_child(Autonomic())