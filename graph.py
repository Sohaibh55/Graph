

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

