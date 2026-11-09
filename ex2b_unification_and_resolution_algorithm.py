"""
Experiment No: 2b
Title: IMPLEMENTATION OF UNIFICATION AND RESOLUTION ALGORITHM
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement unification and resolution algorithm using python.

Scenario:
In an AI-based expert system for automated reasoning, the system needs to resolve queries
by unifying logical predicates and applying resolution inference. For example, given the
knowledge base:
- Rule 1: If John is a human, then John is a mortal -> Human(John) -> Mortal(John)
- Fact 1: Human(John)
- Query: Is John mortal?
"""

import re

# Function to check if two predicates can be unified
def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():  # x is a variable
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():  # y is a variable
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

# Function to unify a variable with a term
def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Function to apply resolution rule
def resolution(kb, query):
    for clause in kb:
        # Check if query matches the head or premise of clause
        for idx, part in enumerate(clause):
            theta = unify(part, query, {})
            if theta is not None:
                # Other parts of clause that need to be resolved
                remaining = [p for i, p in enumerate(clause) if i != idx]
                if not remaining:
                    return True
                else:
                    return resolution(kb, remaining[0])
    return False

if __name__ == "__main__":
    # Knowledge base containing implications and facts
    # Rule: Human(John) -> Mortal(John)
    # Fact: Human(John)
    knowledge_base = [
        [["Human", "John"], ["Mortal", "John"]],  # Human(John) -> Mortal(John)
        [["Human", "John"]]                       # Fact: Human(John)
    ]

    # Query: Mortal(John)?
    query = ["Mortal", "John"]

    # Apply resolution
    if resolution(knowledge_base, query):
        print("Query is resolved: John is Mortal")
    else:
        print("Query could not be resolved")
