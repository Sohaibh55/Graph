from collections import deque
import heapq

class Graph:
    def __init__(self, size):

        self.graph = [[] for _ in range(size)]

    def add_edge(self, u, v, distance, bidirectional=True):

        self.graph[u].append((v, distance))
        if bidirectional:
            self.graph[v].append((u, distance))

    def bfs(self, start_index):
        visited_index = [False] * len(self.graph)
        queue = deque([start_index])
        visited_index[start_index] = True

        print(f"BFS traversal starting from node {start_index}: ", end="")
        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor, _ in self.graph[current]:
                if not visited_index[neighbor]:
                    queue.append(neighbor)
                    visited_index[neighbor] = True
        print()

    def rec_dfs(self, visited_state, start_index):
        print(start_index, end=" ")
        visited_state[start_index] = True

        for neighbor, _ in self.graph[start_index]:
            if not visited_state[neighbor]:
                self.rec_dfs(visited_state, neighbor)

    def dfs(self):
        visited_state = [False] * len(self.graph)
        print("DFS Traversal: ", end="")
        for i in range(len(self.graph)):
            if not visited_state[i]:
                self.rec_dfs(visited_state, i)
        print()

    def dijkstra(self, start_index):
        distances = [float('inf')] * len(self.graph)
        distances[start_index] = 0
        priority_queue = [(0, start_index)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        print(f"Shortest distances from node {start_index}:")
        for i, d in enumerate(distances):
            print(f"Node {i} : Distance {d}")

