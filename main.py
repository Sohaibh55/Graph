import graph

Graph = graph.graph(5)

Graph.insert(0, 1, 3, True)
Graph.insert(0, 2, 5, True)


Graph.insert(1, 3, 8, True)

Graph.insert(2, 3, 9, True)

Graph.insert(4, 1, 10, True)
Graph.insert(4, 3, 15, True)

Graph.display()

Graph.BFS(3)