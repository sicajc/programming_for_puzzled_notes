# Wonderful weekend
- Inviting friends so that friends hating each other would not appear in the same day.
- The relationship of who dislike who is modeled as a relation graph.
- Constraints: Friday and Saturday parties, each friend that dislike each other should not appear at the same day. Check if this is possible and give a valid solution to the scheduling of parties.
# Bipartite graph
1. For there to be a valid scheduling, the graph must be a bipartite graph. For a graph to be bipartite graph, there must not contain any even cycle.
2. To reformulate the problem, for a graph to be a bipartite graph, the graph must be 2-colourable!
3. To color each node with 2 colours s.t. no pair of nodes with an edge between them have the same colours.

# DFS
1. Uses DFS then assign colours to each vertices.