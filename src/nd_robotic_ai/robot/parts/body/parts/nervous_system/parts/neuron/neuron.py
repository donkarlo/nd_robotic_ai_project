from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.action_potential import \
    ActionPotential
from nd_robotic_ai.robot.composition.leaf import Leaf as RobotLeaf
from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.observer.publisher import \
    Publisher as ActionPotentialPublisher
from nd_utility.data.kind.group.decorator.unikinded import Unikinded


class Neuron(RobotLeaf, ActionPotentialPublisher):
    def notify_action_potential_subscribers(self, action_potential:ActionPotential):
        pass

    def fire_action_potential_train(self)->Unikinded[ActionPotential]:
        pass