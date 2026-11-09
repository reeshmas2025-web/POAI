"""
Experiment No: 3b
Title: IMPLEMENTATION OF A FUZZY INFERENCE SYSTEM
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement Fuzzy Inference System.

Scenario:
A company wants to automate employee performance evaluation based on two factors:
1. Work Experience (Years)
2. Project Success Rate (%)

Using Fuzzy Logic, we classify employee performance as Poor, Average, or Excellent,
which helps determine bonuses or promotions.

Rules:
- If experience is low AND success rate is low -> Performance is Poor.
- If experience is medium OR success rate is medium -> Performance is Average.
- If experience is high AND success rate is high -> Performance is Excellent.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def run_fuzzy_inference(exp_val=12, success_val=70):
    # Define fuzzy variables
    experience = ctrl.Antecedent(np.arange(0, 21, 1), 'experience')
    success_rate = ctrl.Antecedent(np.arange(0, 101, 1), 'success_rate')
    performance = ctrl.Consequent(np.arange(0, 101, 1), 'performance')

    # Define fuzzy membership functions
    experience['low'] = fuzz.trimf(experience.universe, [0, 0, 10])
    experience['medium'] = fuzz.trimf(experience.universe, [5, 10, 15])
    experience['high'] = fuzz.trimf(experience.universe, [10, 20, 20])

    success_rate['low'] = fuzz.trimf(success_rate.universe, [0, 0, 50])
    success_rate['medium'] = fuzz.trimf(success_rate.universe, [25, 50, 75])
    success_rate['high'] = fuzz.trimf(success_rate.universe, [50, 100, 100])

    performance['poor'] = fuzz.trimf(performance.universe, [0, 0, 50])
    performance['average'] = fuzz.trimf(performance.universe, [25, 50, 75])
    performance['excellent'] = fuzz.trimf(performance.universe, [50, 100, 100])

    # Define fuzzy rules
    rule1 = ctrl.Rule(experience['low'] & success_rate['low'], performance['poor'])
    rule2 = ctrl.Rule(experience['medium'] | success_rate['medium'], performance['average'])
    rule3 = ctrl.Rule(experience['high'] & success_rate['high'], performance['excellent'])

    # Create FIS control system
    performance_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    performance_sim = ctrl.ControlSystemSimulation(performance_ctrl)

    # Provide input values
    performance_sim.input['experience'] = exp_val       # e.g., 12 years
    performance_sim.input['success_rate'] = success_val  # e.g., 70%

    # Compute fuzzy inference
    performance_sim.compute()

    # Print the output
    print(f"Experience: {exp_val} years, Success Rate: {success_val}%")
    print(f"Predicted Performance Score: {performance_sim.output['performance']:.2f}")

if __name__ == "__main__":
    run_fuzzy_inference(12, 70)
