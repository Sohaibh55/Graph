import graph

Graph = graph.graph(5)

Graph.insert(10, 1, 3, True)
Graph.insert(0, 2, 5, True)

Graph.insert(1, 2, 6, True)
graph.insert(1, 3, 8, True)

Graph.insert(2, 3, 9, True)
Graph.insert(2, 4, 10, True)

graph.display()