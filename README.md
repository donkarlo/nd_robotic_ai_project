# ND Robotic AI

> Life is the active resistance against the collapse of equilibrium.

## Research goal

This repository explores autonomous robots and groups of aerial robots that maintain individual and collective viability while interacting with their environment and other agents. The longer-term goal is sustained migration in search of energy resources, alongside homeostatic/allostatic regulation, active inference, and communication with humans and other robots. **This is a research objective**, not a claim that the entire autonomy framework is implemented.

Python package: **nd_robotic_ai** (src layout).

## Code map

| Area | Location | Current scope |
| --- | --- | --- |
| Robot and group models | src/nd_robotic_ai/robot/; src/nd_robotic_ai/society/ | Robot/composite, swarm, goal, action and experiment structures |
| Perception and state | src/nd_robotic_ai/robot/part/mind/part/cognition/ | Traces, state representations, estimation scaffolds, learning and memory |
| State abstractions | src/nd_robotic_ai/robot/state/state.py; src/nd_robotic_ai/robot/part/mind/part/cognition/part/object_level/process/part/perception/state/ | NumPy-backed State, vector-representable State, partial estimators |
| Neural and sensor models | src/nd_robotic_ai/robot/part/body/part/nervous_system/ | Action-potential / waveform experiments and GPS–LiDAR modelling prototypes |
| ROS | src/nd_robotic_ai/platform/ros/ | Message, frames, bags/YAML, LiDAR and odometry-related representations |
| Reminders and plans | src/nd_robotic_ai/robot/part/mind/part/cognition/part/object_level/process/part/memory/part/explicit/part/short_term/part/plan/reminder/ | PySide6 planner/reminder interface, schedule loaders and speech |
| UAV and environment | src/nd_robotic_ai/robot/kind/ | UAV, human and environment models |

The codebase contains implemented utilities, research prototypes, interfaces and placeholders. For instance, the perceptual state-estimation Estimator stores sensor observations but is not yet a complete filtering implementation; Odometry.get_pose is a placeholder. There are multiple distinct State classes, not a single integrated self-state architecture.

## Relationship with the other ND projects

- **nd_math_project**: mathematical objects, distributions, geometry and time-series operations.
- **nd_physics_project**: quantities, units, pose, twist and physical-state representations.
- **nd_sociomind_project**: multi-agent experiments; several neural/sensor modules consume its recordings.
- **nd_robotic_ai_learning_project**: LaTeX conceptual and literature notes, separate from this Python runtime.

Other imports reference nd_utility, NumPy, SciPy, Matplotlib, PySide6, TensorFlow and related research packages. Not all are specified in the packaging metadata.

## Development

The package metadata is in pyproject.toml. In a Python environment with the needed cross-project dependencies:

~~~bash
python -m pip install -e .
python -m pytest tests
~~~

Running the test suite is a development check, **not** evidence that every research subsystem works. The declared robotix console entry points to nd_robotic_ai.__main__:main, but the corresponding __main__.py is empty. Do not rely on that CLI without implementing its target.

## Current limitations

- The active-inference/homeostasis narrative is a research goal and is not an end-to-end verified implementation.
- A static syntax scan identified four tracked Python modules with syntax errors. Other files include incomplete methods or imports specific to the multi-repository research environment.
- Package requirements currently declare ruamel.yaml, not every library required by experiments or user interfaces.
- The root LICENSE file is empty; no licensing terms are implied by this README.
