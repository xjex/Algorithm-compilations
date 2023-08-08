class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        if node in self.graph:
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = {node: False for node in self.graph}
        self.dfs(start_node, visited)


# Example usage
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
graph.add_edge(3, 7)

start_node = 1
print("DFS Traversal:")
graph.dfs_traversal(start_node)
