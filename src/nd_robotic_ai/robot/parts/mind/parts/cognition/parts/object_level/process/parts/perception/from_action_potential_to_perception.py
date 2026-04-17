class FromActionPotentialToPerception:
    def __init__(self):
        pass

from abc import ABC, abstractmethod
from typing import List, Optional


class ActionPotentialEvent:

    def __init__(self, neuron_id: int, timestamp_milliseconds: float, amplitude_millivolts: float):
        self.neuron_id = neuron_id
        self.timestamp_milliseconds = timestamp_milliseconds
        self.amplitude_millivolts = amplitude_millivolts


class SpikeWindow:

    def __init__(self, start_time_milliseconds: float, end_time_milliseconds: float,
                 spikes: List[ActionPotentialEvent]):
        self.start_time_milliseconds = start_time_milliseconds
        self.end_time_milliseconds = end_time_milliseconds
        self.spikes = spikes


class PopulationPattern:

    def __init__(self, neuron_count: int, spike_counts_per_neuron: List[int], total_spike_count: int):
        self.neuron_count = neuron_count
        self.spike_counts_per_neuron = spike_counts_per_neuron
        self.total_spike_count = total_spike_count


class FeatureVector:

    def __init__(self, values: List[float]):
        self.values = values


class LabeledPercept:

    def __init__(self, label: str, confidence: float):
        self.label = label
        self.confidence = confidence


class Filter(ABC):

    @abstractmethod
    def process(self, data: object) -> object:
        pass


class SpikeCollectorFilter(Filter):

    def __init__(self, window_size_milliseconds: float, neuron_count: int):
        self._window_size_milliseconds = window_size_milliseconds
        self._neuron_count = neuron_count
        self._buffer: List[ActionPotentialEvent] = []
        self._window_start_time_milliseconds: Optional[float] = None

    def process(self, data: object) -> object:
        if not isinstance(data, ActionPotentialEvent):
            raise TypeError("SpikeCollectorFilter expects an ActionPotentialEvent.")

        spike_event = data

        if self._window_start_time_milliseconds is None:
            self._window_start_time_milliseconds = spike_event.timestamp_milliseconds

        self._buffer.append(spike_event)

        elapsed_time = spike_event.timestamp_milliseconds - self._window_start_time_milliseconds

        if elapsed_time < self._window_size_milliseconds:
            return None

        spike_window = SpikeWindow(
            start_time_milliseconds=self._window_start_time_milliseconds,
            end_time_milliseconds=spike_event.timestamp_milliseconds,
            spikes=list(self._buffer)
        )

        self._buffer.clear()
        self._window_start_time_milliseconds = None
        return spike_window


class PopulationPatternBuilderFilter(Filter):

    def __init__(self, neuron_count: int):
        self._neuron_count = neuron_count

    def process(self, data: object) -> object:
        if data is None:
            return None

        if not isinstance(data, SpikeWindow):
            raise TypeError("PopulationPatternBuilderFilter expects a SpikeWindow.")

        spike_window = data
        spike_counts_per_neuron = [0 for _ in range(self._neuron_count)]

        for spike in spike_window.spikes:
            if 0 <= spike.neuron_id < self._neuron_count:
                spike_counts_per_neuron[spike.neuron_id] += 1

        total_spike_count = sum(spike_counts_per_neuron)

        return PopulationPattern(
            neuron_count=self._neuron_count,
            spike_counts_per_neuron=spike_counts_per_neuron,
            total_spike_count=total_spike_count
        )


class FeatureExtractionFilter(Filter):

    def process(self, data: object) -> object:
        if data is None:
            return None

        if not isinstance(data, PopulationPattern):
            raise TypeError("FeatureExtractionFilter expects a PopulationPattern.")

        population_pattern = data

        if population_pattern.neuron_count == 0:
            mean_spike_rate = 0.0
        else:
            mean_spike_rate = population_pattern.total_spike_count / population_pattern.neuron_count

        active_neuron_count = 0
        for spike_count in population_pattern.spike_counts_per_neuron:
            if spike_count > 0:
                active_neuron_count += 1

        feature_values = [
            float(population_pattern.total_spike_count),
            float(active_neuron_count),
            float(mean_spike_rate)
        ]

        return FeatureVector(feature_values)


class PerceptionLabelFilter(Filter):

    def process(self, data: object) -> object:
        if data is None:
            return None

        if not isinstance(data, FeatureVector):
            raise TypeError("PerceptionLabelFilter expects a FeatureVector.")

        feature_vector = data
        total_spike_count = feature_vector.values[0]
        active_neuron_count = feature_vector.values[1]

        if total_spike_count >= 5 and active_neuron_count >= 3:
            label = "touch_detected"
            confidence = 0.90
        else:
            label = "no_touch"
            confidence = 0.60

        return LabeledPercept(label, confidence)


class Pipeline:

    def __init__(self):
        self._filters: List[Filter] = []

    def add_filter(self, filter_object: Filter) -> None:
        self._filters.append(filter_object)

    def process(self, data: object) -> object:
        current_data = data

        for filter_object in self._filters:
            current_data = filter_object.process(current_data)

            if current_data is None:
                return None

        return current_data


class Demo:

    def run(self) -> None:
        pipeline = Pipeline()
        pipeline.add_filter(SpikeCollectorFilter(window_size_milliseconds=10.0, neuron_count=5))
        pipeline.add_filter(PopulationPatternBuilderFilter(neuron_count=5))
        pipeline.add_filter(FeatureExtractionFilter())
        pipeline.add_filter(PerceptionLabelFilter())

        spike_stream = [
            ActionPotentialEvent(0, 0.0, 80.0),
            ActionPotentialEvent(1, 2.0, 76.0),
            ActionPotentialEvent(2, 4.0, 79.0),
            ActionPotentialEvent(1, 7.0, 81.0),
            ActionPotentialEvent(3, 11.0, 77.0),
            ActionPotentialEvent(0, 20.0, 75.0),
            ActionPotentialEvent(0, 22.0, 74.0),
        ]

        for spike_event in spike_stream:
            result = pipeline.process(spike_event)

            if isinstance(result, LabeledPercept):
                print("Label:", result.label)
                print("Confidence:", result.confidence)
                print("---")


if __name__ == "__main__":
    Demo().run()