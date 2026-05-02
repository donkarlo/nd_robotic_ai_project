from __future__ import annotations

import math
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy
from scipy.optimize import differential_evolution
from scipy.optimize import least_squares


class FmmComponentParameters:
    def __init__(self, amplitude: float, alpha: float, beta: float, omega: float) -> None:
        self.amplitude = amplitude
        self.alpha = alpha
        self.beta = beta
        self.omega = omega

    def get_as_list(self) -> List[float]:
        return [
            self.amplitude,
            self.alpha,
            self.beta,
            self.omega
        ]


class SingleFmmSignalParameters:
    def __init__(self, baseline: float, component_parameters: FmmComponentParameters) -> None:
        self.baseline = baseline
        self.component_parameters = component_parameters

    def get_as_list(self) -> List[float]:
        return [
            self.baseline,
            self.component_parameters.amplitude,
            self.component_parameters.alpha,
            self.component_parameters.beta,
            self.component_parameters.omega
        ]


class FmmComponent:
    def __init__(self, parameters: FmmComponentParameters) -> None:
        self.parameters = parameters

    def evaluate(self, time_points: numpy.ndarray) -> numpy.ndarray:
        phase = (
                self.parameters.beta
                +
                2.0
                *
                numpy.arctan(
                    self.parameters.omega
                    *
                    numpy.tan(
                        (time_points - self.parameters.alpha) / 2.0
                    )
                )
        )

        values = self.parameters.amplitude * numpy.cos(phase)
        return values


class TwoComponentFmmSignal:
    def __init__(self, baseline: float, first_component: FmmComponent, second_component: FmmComponent) -> None:
        self.baseline = baseline
        self.first_component = first_component
        self.second_component = second_component

    def evaluate_first_wave(self, time_points: numpy.ndarray) -> numpy.ndarray:
        values = self.first_component.evaluate(time_points)
        return values

    def evaluate_second_wave(self, time_points: numpy.ndarray) -> numpy.ndarray:
        values = self.second_component.evaluate(time_points)
        return values

    def evaluate(self, time_points: numpy.ndarray) -> numpy.ndarray:
        values = (
                self.baseline
                +
                self.first_component.evaluate(time_points)
                +
                self.second_component.evaluate(time_points)
        )

        return values


class SingleFmmSignal:
    def __init__(self, parameters: SingleFmmSignalParameters) -> None:
        self.parameters = parameters
        self.component = FmmComponent(parameters.component_parameters)

    def evaluate(self, time_points: numpy.ndarray) -> numpy.ndarray:
        values = self.parameters.baseline + self.component.evaluate(time_points)
        return values


class FmmParameterVectorFactory:
    def create_single_fmm_parameters_from_vector(self, parameter_vector: numpy.ndarray) -> SingleFmmSignalParameters:
        baseline = float(parameter_vector[0])
        amplitude = float(parameter_vector[1])
        alpha = float(parameter_vector[2])
        beta = float(parameter_vector[3])
        omega = float(parameter_vector[4])

        component_parameters = FmmComponentParameters(
            amplitude,
            alpha,
            beta,
            omega
        )

        parameters = SingleFmmSignalParameters(
            baseline,
            component_parameters
        )

        return parameters


class SingleFmmFitObjective:
    def __init__(self, time_points: numpy.ndarray, target_values: numpy.ndarray) -> None:
        self.time_points = time_points
        self.target_values = target_values
        self.parameter_vector_factory = FmmParameterVectorFactory()

    def compute_residuals(self, parameter_vector: numpy.ndarray) -> numpy.ndarray:
        parameters = self.parameter_vector_factory.create_single_fmm_parameters_from_vector(parameter_vector)
        signal = SingleFmmSignal(parameters)
        predicted_values = signal.evaluate(self.time_points)
        residuals = self.target_values - predicted_values
        return residuals

    def compute_sum_of_squared_errors(self, parameter_vector: numpy.ndarray) -> float:
        residuals = self.compute_residuals(parameter_vector)
        squared_errors = residuals ** 2
        sum_of_squared_errors = float(numpy.sum(squared_errors))
        return sum_of_squared_errors


class SingleFmmParameterBounds:
    def __init__(self, target_values: numpy.ndarray) -> None:
        target_minimum = float(numpy.min(target_values))
        target_maximum = float(numpy.max(target_values))
        signal_range = target_maximum - target_minimum

        if signal_range <= 0.0:
            signal_range = 1.0

        self.baseline_lower = target_minimum - signal_range
        self.baseline_upper = target_maximum + signal_range
        self.amplitude_lower = 0.0
        self.amplitude_upper = 2.0 * signal_range
        self.alpha_lower = 0.0
        self.alpha_upper = 2.0 * math.pi
        self.beta_lower = 0.0
        self.beta_upper = 2.0 * math.pi
        self.omega_lower = 0.001
        self.omega_upper = 1.0

    def get_differential_evolution_bounds(self) -> List[Tuple[float, float]]:
        bounds = [
            (self.baseline_lower, self.baseline_upper),
            (self.amplitude_lower, self.amplitude_upper),
            (self.alpha_lower, self.alpha_upper),
            (self.beta_lower, self.beta_upper),
            (self.omega_lower, self.omega_upper)
        ]

        return bounds

    def get_least_squares_bounds(self) -> Tuple[numpy.ndarray, numpy.ndarray]:
        lower_bounds = numpy.array(
            [
                self.baseline_lower,
                self.amplitude_lower,
                self.alpha_lower,
                self.beta_lower,
                self.omega_lower
            ],
            dtype=float
        )

        upper_bounds = numpy.array(
            [
                self.baseline_upper,
                self.amplitude_upper,
                self.alpha_upper,
                self.beta_upper,
                self.omega_upper
            ],
            dtype=float
        )

        return lower_bounds, upper_bounds


class SingleFmmFitResult:
    def __init__(self, parameters: SingleFmmSignalParameters, sum_of_squared_errors: float) -> None:
        self.parameters = parameters
        self.sum_of_squared_errors = sum_of_squared_errors

    def create_signal(self) -> SingleFmmSignal:
        signal = SingleFmmSignal(self.parameters)
        return signal

    def print_summary(self) -> None:
        print("Best five parameters for one FMM wave:")
        print("M      =", self.parameters.baseline)
        print("A      =", self.parameters.component_parameters.amplitude)
        print("alpha  =", self.parameters.component_parameters.alpha)
        print("beta   =", self.parameters.component_parameters.beta)
        print("omega  =", self.parameters.component_parameters.omega)
        print("SSE    =", self.sum_of_squared_errors)


class SingleFmmWaveFitter:
    def __init__(self, maximum_iterations: int, random_seed: int) -> None:
        self.maximum_iterations = maximum_iterations
        self.random_seed = random_seed
        self.parameter_vector_factory = FmmParameterVectorFactory()

    def fit(self, time_points: numpy.ndarray, target_values: numpy.ndarray) -> SingleFmmFitResult:
        objective = SingleFmmFitObjective(time_points, target_values)
        bounds = SingleFmmParameterBounds(target_values)

        global_result = differential_evolution(
            objective.compute_sum_of_squared_errors,
            bounds.get_differential_evolution_bounds(),
            maxiter=self.maximum_iterations,
            seed=self.random_seed,
            polish=False
        )

        local_result = least_squares(
            objective.compute_residuals,
            global_result.x,
            bounds=bounds.get_least_squares_bounds(),
            max_nfev=5000
        )

        best_parameter_vector = local_result.x
        best_parameters = self.parameter_vector_factory.create_single_fmm_parameters_from_vector(best_parameter_vector)
        best_error = objective.compute_sum_of_squared_errors(best_parameter_vector)

        result = SingleFmmFitResult(best_parameters, best_error)
        return result


class FmmWavePlotter:
    def plot(self, time_points: numpy.ndarray, first_wave_values: numpy.ndarray, second_wave_values: numpy.ndarray,
             combined_wave_values: numpy.ndarray, fitted_wave_values: numpy.ndarray) -> None:
        figure, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

        axes[0].plot(time_points, first_wave_values)
        axes[0].set_title("First FMM wave")
        axes[0].set_ylabel("Value")
        axes[0].grid(True)

        axes[1].plot(time_points, second_wave_values)
        axes[1].set_title("Second FMM wave")
        axes[1].set_ylabel("Value")
        axes[1].grid(True)

        axes[2].plot(time_points, combined_wave_values, label="Combined two-wave signal")
        axes[2].plot(time_points, fitted_wave_values, linestyle="--", label="Fitted single five-parameter wave")
        axes[2].set_title("Combined signal and fitted single FMM wave")
        axes[2].set_xlabel("Time")
        axes[2].set_ylabel("Value")
        axes[2].legend()
        axes[2].grid(True)

        plt.tight_layout()
        plt.show()


class ExampleApplication:
    def __init__(self) -> None:
        self.sample_count = 1000
        self.time_start = 0.0
        self.time_end = 2.0 * math.pi

    def create_time_points(self) -> numpy.ndarray:
        time_points = numpy.linspace(
            self.time_start,
            self.time_end,
            self.sample_count,
            endpoint=False
        )

        return time_points

    def create_two_component_signal(self) -> TwoComponentFmmSignal:
        first_component_parameters = FmmComponentParameters(
            30.0,
            1.0,
            0.5,
            0.30
        )

        second_component_parameters = FmmComponentParameters(
            15.0,
            2.3,
            4.0,
            0.70
        )

        first_component = FmmComponent(first_component_parameters)
        second_component = FmmComponent(second_component_parameters)

        signal = TwoComponentFmmSignal(
            -70.0,
            first_component,
            second_component
        )

        return signal

    def run(self) -> None:
        time_points = self.create_time_points()
        two_component_signal = self.create_two_component_signal()

        first_wave_values = two_component_signal.evaluate_first_wave(time_points)
        second_wave_values = two_component_signal.evaluate_second_wave(time_points)
        combined_wave_values = two_component_signal.evaluate(time_points)

        fitter = SingleFmmWaveFitter(
            500,
            42
        )

        fit_result = fitter.fit(time_points, combined_wave_values)
        fit_result.print_summary()

        fitted_single_signal = fit_result.create_signal()
        fitted_wave_values = fitted_single_signal.evaluate(time_points)

        plotter = FmmWavePlotter()
        plotter.plot(
            time_points,
            first_wave_values,
            second_wave_values,
            combined_wave_values,
            fitted_wave_values
        )


if __name__ == "__main__":
    application = ExampleApplication()
    application.run()