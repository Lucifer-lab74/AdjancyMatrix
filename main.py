# Import numpy for Adjacency matrix
import numpy as np
# Main class graph
class Graph:

    # Constructor
    # Takes number of nodes
    def __init__(self, N):
        # default params
        self.vert_list = []
        # Create adj matrix of N * N zeros..This is due to numpy arrays are immutatble.
        self.adj_matrix = np.array(np.zeros((N, N), dtype=int))

    # function to add an edge to graph
    def add_edge(self, v1, v2):
        # Check whether vertex is already in the list or not
        # if not then add respective vertex to list
        if v1 not in self.vert_list:
            self.add_vertex(v1)
        elif v2 not in self.vert_list:
            self.add_vertex(v2)

        # As graph starts with 1 but array initiate with zero
        # we add 1 that represent edge is present at index before each vertex
        self.adj_matrix[v1 - 1][v2 - 1] = 1
        self.adj_matrix[v2 - 1][v1 - 1] = 1

    # Function to add edge
    def add_vertex(self, key):
        # check if key is present in list or not
        if key not in self.vert_list:
            self.vert_list.append(key)

    # Return the vertices list which are connected
    def __str__(self):
        visited = []
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[0])):
                if self.adj_matrix[i][j] == 1:
                    # If value is one the it means edge is present at those indices
                    if [j+1, i+1] not in visited:
                        visited.append([i+1, j+1])

        return visited


# Create new instance of class graph
g = Graph(6)
# Add some vertices
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
# Add edges between them
g.add_edge(1, 2)
g.add_edge(1, 5)
g.add_edge(2, 5)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(5, 4)
# Here vertex 6 is directly gets added
g.add_edge(4, 6)

print(g.__str__())


#--output--for sample graph
# [[1, 2], [1, 5], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6]]

