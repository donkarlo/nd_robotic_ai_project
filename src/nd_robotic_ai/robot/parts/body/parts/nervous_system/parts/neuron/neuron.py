from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.action_potential import \
    ActionPotential
from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeUnit
from nd_utility.data.kind.group.decorator.unikinded import Unikinded
from nd_utility.data.kind.group.group import Group


class Neuron(RobotCompositeUnit):
    def fire_single_action_potential(self, action_potential:ActionPotential):
        pass

    def fire_action_potential_train(self)->Unikinded[ActionPotential]:
        pass