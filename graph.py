
import queue
class graph :
    def __init__(self,size):
        self.graph = [ [ 0 for _ in range(size)] for _ in range(size) ]
    def insert(self,u,v,distance,allow):
        assert 0 <= u < len(self.graph) and  0 <= v <len(self.graph), " Error : Invalid index "
        self.graph[u][v] = distance
        if allow :
            self.graph[v][u] = distance
    def display(self):
        for i in  range(len(self.graph)) :
           print(f"{i} : ",end="")
           for j in  range(len(self.graph)) :
               if  self.graph[i][j] != 0 :
                   print(f" ( {j},{self.graph[i][j]} ) ",end='')
           print()
    def BFS(self,start_index):
        vertex_index = [True if _ == start_index  else False for _ in range(len(self.graph)) ]
        Queue = queue.Queue()
        Queue.put(start_index)
        print(f"BFS traversal starting from node {start_index} : ",end="")
        while not Queue.empty() :

            start_index = Queue.get()
            print(start_index,end=" ")

            for i in range(len(self.graph)) :
                if not vertex_index[i] and self.graph[start_index][i]:
                    Queue.put(i)
                    vertex_index[i] = True


