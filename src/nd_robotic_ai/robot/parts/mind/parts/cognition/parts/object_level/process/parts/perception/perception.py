from typing import Optional

from nd_robotic_ai.robot.composition.composite import Composite as RobotCompositeComponent
from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.action_potential import \
    ActionPotential
from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.observer.subscriber import \
    Subscriber as ActionPotentialSubcriber
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.observer.kind.trace_formation.publisher import \
    Publisher as PerceptionPublisher
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.observer.kind.trace_formation.subscriber import \
    Subscriber as PerceptionSubscriber
from nd_robotic_ai.robot.parts.mind.parts.cognition.parts.object_level.process.parts.perception.trace.trace import Trace
from nd_utility.oop.design_pattern.architectural.pipes_and_filters.pipes_and_filters import PipesAndFilters
from nd_utility.oop.design_pattern.structural.composition.composite import Composite as BaseComposite
from nd_utility.oop.inheritance.overriding import override_from


class Perception(RobotCompositeComponent, ActionPotentialSubcriber, PerceptionPublisher):
    """
    Should I add the current observation point to a meaning ful group and create an abstract concept or should I pass it as it is planning?
    - Perception cqn be conceious and unconcious
    """

    def __init__(self):
        RobotCompositeComponent.__init__(self)

        self._action_potential_composite = BaseComposite()
        self._pipes_and_filters = PipesAndFilters()

        self._subscribers = []

    @override_from(ActionPotentialSubcriber, False, False)
    def handle_new_action_potential(self, action_potential: ActionPotential) -> Optional[Trace]:
        self._sort_action_potentials(action_potential)

    def attach_subcriber(self, subscriber: PerceptionSubscriber):
        self._subscribers.append(subscriber)

    def notify_subscribers(self) -> None:
        for subscriber in self._subscribers:
            subscriber.notify_subscribers()

    def _sort_action_potential(self, action_potential: ActionPotential):
        """
        - see sorting action potentials
        Fine out to which branch in self._action_potential_composite   the new action potential belongs acoording to its shape
        Args:
            action_potential:

        Returns:

        """
        generating_neural_coding_is_necessary = False
        if generating_neural_coding_is_necessary:
            self._generate_neural_coding()

    def _generate_neural_coding(self):
        """
        Returns:

        """
        pass
