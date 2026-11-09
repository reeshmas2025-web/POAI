"""
Experiment: Decision Making and Knowledge Representation (Python Simulation)
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement decision making and knowledge representation in Python simulating Prolog logic.
"""

def minimum(x, y):
    if x <= y:
        return x
    return y

def maximum(x, y):
    if x >= y:
        return x
    return y

# Facts
facts = {
    ("mary", "food"),
    ("mary", "wine"),
    ("john", "wine"),
    ("john", "mary")
}

def likes(person, item):
    # Direct fact check
    if (person, item) in facts:
        return True
    
    if person == "john":
        # Rule 1: John likes anything that Mary likes
        if ("mary", item) in facts:
            return True
        # Rule 2: John likes anyone who likes wine
        if (item, "wine") in facts:
            return True
        # Rule 3: John likes anyone who likes themselves
        if (item, item) in facts:
            return True
            
    return False

def find_who_john_likes():
    entities = ["mary", "john", "wine", "food"]
    return [e for e in entities if likes("john", e)]

if __name__ == "__main__":
    print("--- Part 1: Minimum and Maximum ---")
    print(f"minimum(5, 10) = {minimum(5, 10)}")
    print(f"maximum(5, 10) = {maximum(5, 10)}")
    print(f"minimum(8, 3) = {minimum(8, 3)}, maximum(8, 3) = {maximum(8, 3)}")

    print("\n--- Part 2: Knowledge Representation Queries ---")
    print(f"?- likes(mary, food): {'yes' if likes('mary', 'food') else 'no'}")
    print(f"?- likes(john, wine): {'yes' if likes('john', 'wine') else 'no'}")
    print(f"?- likes(john, food): {'yes' if likes('john', 'food') else 'no'}")
    print(f"?- likes(john, Y): {find_who_john_likes()}")
