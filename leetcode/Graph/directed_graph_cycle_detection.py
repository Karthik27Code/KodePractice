from collections import defaultdict

def detect_cycle(graph: dict[str, list]):
    color = defaultdict(int)

    for node in graph.keys():
        if color[node] == 0:
            stack = [node]

            while stack:
                cur_node = stack[-1]
                if color[cur_node] == 0:
                    color[cur_node] = 1

                    # Add neighbors to the stack in reverse order to maintain DFS order
                    neighbors = graph.get(cur_node, [])
                    for neighbor in reversed(neighbors):
                        if color[neighbor] == 0:
                            stack.append(neighbor)
                        elif color[neighbor] == 1:
                            return True
                else:
                    cur_node = stack.pop()
                    color[cur_node] = 2
    return False

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': []
}

print(detect_cycle(graph=graph))