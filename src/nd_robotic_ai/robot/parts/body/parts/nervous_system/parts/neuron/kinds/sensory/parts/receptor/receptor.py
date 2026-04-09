from nd_robotic_ai.robot.composition.leaf import Leaf as RobotLeaf
from nd_robotic_ai.robot.parts.body.parts.nervous_system.parts.neuron.kinds.sensory.parts.receptor.observer.publisher import \
    Publisher as ObservationPublisher


class Receptor(RobotLeaf, ObservationPublisher):
    """
    #Receptor
    """
    def __init__(self):
     self._new_observation_subscribers = []

    def attach_new_abservation_subscriber(self, subscriber)->None:
        self._new_observation_subscribers.append(subscriber)

    def publish_new_observation(self, observation)->None:
        for new_observation_subscriber  in self._new_observation_subscribers:
            new_observation_subscriber.handle_new_observation(observation)

