"""
Experiment No: 2c
Title: IMPLEMENTATION OF BACKWARD CHAINING
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement backward chaining.

Scenario:
A medical expert system is designed to diagnose diseases based on patient symptoms. The
system uses backward chaining to infer whether a patient has a specific disease by checking
rules and known facts.
"""

# Knowledge Base (Rules in IF-THEN format)
knowledge_base = {
    "flu": [["cough", "fever"]],
    "fever": [["sore_throat"]],
}

# Known facts
facts = {"sore_throat", "cough"}

# Backward chaining function
def backward_chaining(goal):
    if goal in facts:  # If the goal is a known fact, return True
        return True

    if goal in knowledge_base:  # If the goal has rules in KB
        for conditions in knowledge_base[goal]:  # Check each rule
            if all(backward_chaining(cond) for cond in conditions):  # Recursively verify
                return True

    return False  # If no rule or fact supports the goal, return False

if __name__ == "__main__":
    # Query: Does the patient have flu?
    query = "flu"

    if backward_chaining(query):
        print(f"The patient is diagnosed with {query}.")
    else:
        print(f"The patient does NOT have {query}.")
