from nd_robotic_ai.experiment.condition.kind.event_specific_knowledge import EventSpecificKnowledge as EventSpecificKnowledgeCondition
from nd_robotic_ai.experiment.kind.train_test.train_test import TrainTest


class EventSpecificKnowledge(TrainTest):
    def __init__(self, train_esk_condition: EventSpecificKnowledgeCondition,
                 test_esk_condition: EventSpecificKnowledgeCondition):
        self._train_esk_condition = train_esk_condition
        self._test_esk_condition = test_esk_condition
