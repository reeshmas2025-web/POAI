"""
Experiment: Depth First Search
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
To implement depth first search.

Case Scenario:
A robotic delivery system is implemented in a smart warehouse. The warehouse is modeled
as a graph, where each node represents a storage unit and each edge represents a possible
path. The robot needs to pick up a package from a starting point and deliver it to the correct
storage location using Depth First Search (DFS).
"""

# Depth First Search (DFS) implementation for a warehouse graph
# Sample warehouse graph as an adjacency list
warehouse_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Function to perform DFS
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    # Mark current node as visited and add to path
    visited.add(start)
    path.append(start)

    # If goal is found, return the path
    if start == goal:
        return path

    # Explore neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path[:])  # Use path[:] to copy path
            if result:  # Stop if a path is found
                return result

    return None  # No path found

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'F'
    path_found = dfs(warehouse_graph, start_node, goal_node)
    print(f"DFS Path from {start_node} to {goal_node}: {path_found}")
