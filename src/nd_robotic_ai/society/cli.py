from nd_utility.ui.cli.cli import Cli as BaseCli
from nd_robotic_ai.lab.experiment import Experiment


class Cli(BaseCli):
    def run(self):
        if self._args[0] == "xpr":
            pass
