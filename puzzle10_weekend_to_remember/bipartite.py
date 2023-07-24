#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.

# Adjacency graph representation
graph = {'B': ['C'],
         'C': ['B', 'D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D', 'G', 'H', 'I'],
         'G': ['F'],
         'H': ['F'],
         'I': ['F']}

graph2 = {'F': ['D', 'I', 'G', 'H'],
         'B': ['C'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'H': ['F'],
         'C': ['D', 'B'],
         'G': ['F'],
         'I': ['F']}

gra3 = {'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']}

grap = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

def bipartiteGraphColor(graph, start, coloring, color):
    # Recursive calls of bipartite graph colour function
    # This employs dfs for checking the graph is 2 colourable or not.

    # Base Case
    if start not in graph:
        return False, {}

    if start not in coloring:
        # Colouring in a dictionary which stores the number of that particular vertex.
        coloring[start] = color
    elif coloring[start] != color:
        return False, {}
    else:
        return True, coloring

    # Assign the colour to the vertex.
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'

    # DFS recursive call to check to see if the color is 2-coloarable.
    for vertex in graph[start]:
        # For every neighbor for this particular vertex, search deeper for it.
        val, coloring = bipartiteGraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}

    return True, coloring

print (bipartiteGraphColor(gra3, 'A', {}, 'Sha'))
print (bipartiteGraphColor(graph, 'B', {}, 'Sha'))
print (bipartiteGraphColor(graph2, 'B', {}, 'Sha'))
print (bipartiteGraphColor(grap, 'A', {}, 'Sha'))