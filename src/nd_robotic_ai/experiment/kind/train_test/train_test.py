from nd_robotic_ai.experiment.condition.condition import Condition
from nd_robotic_ai.experiment.experiment import Experiment


class TrainTest(Experiment):
    def __init__(self, train_condition:Condition, test_condition:Condition):
        self._train_condition = train_condition
        self._test_condition = test_condition
