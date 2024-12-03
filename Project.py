class Edge:
    def _init_(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Function to find the parent of a node 
def find_parent(parent, node):
    
    if parent[node] == node:
        return node
    
    parent[node] = find_parent(parent, parent[node]) 
    return parent[node]



#  perform union of two subsets
def union_sets(parent, rank, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x] += 1



def kruskal_mst(edges, V):
    edges = sorted(edges, key=lambda edge: edge.weight)    
    # Sort edges based on their weight
    parent = [i for i in range(V)]
    rank = [0] * V
    result = []  

    for edge in edges:
        u = edge.src
        v = edge.dest
        w = edge.weight
 
        root_u = find_parent(parent, u)         
        # check is this make the cycle
        root_v = find_parent(parent, v)

        if root_u != root_v:
            result.append(edge)
            union_sets(parent, rank, root_u, root_v)
        if len(result) == V - 1:
            break

    # MST Printing
    print("Edges in the MST:")
    for edge in result:
        print(f"{edge.src} -- {edge.dest} == {edge.weight}")

if _name_ == "_main_":
    V = 4  
    E = 5  
    edges = [
        Edge(0, 1, 10),
        Edge(0, 2, 6),
        Edge(0, 3, 5),
        Edge(1, 3, 15),
        Edge(2, 3, 4),
    ]
    kruskal_mst(edges, V)
