from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit
from nd_robotic_ai.society.composition.composite.action.kind.communicating.neuron.spike import Spike


class Neuron(RobotCompositeUnit):
    def fire_spike(self, spike:Spike):
        pass