from nd_robotic_ai.experiment.condition.condition import Condition
from nd_robotic_ai.robot.composition.kind.mind.meta_cognition.cognition.process.composition.child.memory.composition.kind.explicit.kind.long_term.episodic.autobigraphical.kind.event_specific_knowledge.event_specific_knowledge import EventSpecificKnowledge as EventSpecificKnowledgeMemory


class EventSpecificKnowledge(Condition):
    def __init__(self, event_specific_knowledge_memory: EventSpecificKnowledgeMemory):
        self._event_specific_knowledge_memory = event_specific_knowledge_memory
        
