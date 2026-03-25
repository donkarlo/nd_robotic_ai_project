
from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.neuron.kinds.sensory.sensory import Sensory
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit
from nd_utility.oop.design_pattern.structural.composition.component import Component


class Somatic(RobotCompositeUnit):
    def __init__(self):
        RobotCompositeUnit.__init__(self)