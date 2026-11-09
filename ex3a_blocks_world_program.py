"""
Experiment No: 3a
Title: IMPLEMENTATION OF BLOCKS WORLD PROGRAM
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement Blocks World Program.

Scenario:
A robotic arm in a warehouse is programmed to rearrange blocks according to a given goal
state. The Blocks World problem involves moving blocks from an initial configuration to a
desired goal configuration while following specific constraints.

Initial State:
A is on B
B is on table
C is on table

Goal State:
B is on C
A is on B
C is on table
"""

class BlocksWorld:
    def __init__(self):
        self.state = {
            "A": "B",      # A is on B
            "B": "table",  # B is on table
            "C": "table"   # C is on table
        }
        self.goal = {
            "A": "B",
            "B": "C",
            "C": "table"
        }

    def is_goal_state(self):
        return self.state == self.goal

    def move(self, block, destination):
        if block in self.state and self.state[block] != destination:
            print(f"Moving {block} from {self.state[block]} to {destination}")
            self.state[block] = destination

    def plan_moves(self):
        print("\nInitial State:", self.state)
        while not self.is_goal_state():
            for block, target in self.goal.items():
                if self.state[block] != target:
                    self.move(block, target)
        print("\nFinal Goal State Reached:", self.state)

if __name__ == "__main__":
    # Run the Blocks World Solver
    bw = BlocksWorld()
    bw.plan_moves()
