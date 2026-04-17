from nd_robotic_ai.robot.parts.body.parts.nervous_system.neural_coding.action_potential.observer.publisher import \
    Publisher as ObservationPublisher
from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.neuron.neuron import Neuron


class Receptor(Neuron, ObservationPublisher):
    """
    #Receptor
    """
    def __init__(self):
     self._new_observation_subscribers = []

    def attach_new_abservation_subscriber(self, subscriber)->None:
        self._new_observation_subscribers.append(subscriber)

    def fire_action_potential(self, observation)->None:
        for new_observation_subscriber  in self._new_observation_subscribers:
            new_observation_subscriber.handle_new_action_potential(observation)

