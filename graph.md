## Basics
Graph = Vertices + Edges
directed vs. undirected

### Application
web crawling (google)
social networking (facebook)
model checking (AI state machine)

### Representation
* dict + list
..* dict of all vertices with their id
..* one vertice  with a list of its neighbors
_variations_
* a list table of vertices with linked list of neighbors
* objects of g, v, e


* v * v matrics

## Search
explore the graph
* BFS and DFS

## Shortest Path
* one vertice level to source is its shortest path number
* any path along a S.P. is a S.P.

### DFS
* parenthesis structure
* can compute strongly connected component

#### Edge types
* tree edge: main search track
* back edge: edge goes back to ancestor, considered a loop
* forward edge: leap to a descendent
* cross edge: all other edges, cross the sub tree

## Shortest Path

### Bellman Ford
* general case: can have negetive weight, cycles, etc.
* bigO(VE): loop v times, relax all edges for each loop

### if Directed Acyclic Graph
* bigo(V+E): do a toposort and relax v's edges in toposort order

### Dijkstra
* non-negetive weights
* can search from two ends to speed up the process

### A * Search
* with hueristics


## Minimum Spanning Tree
* given a undirected weighted graph, find minimum weighted tree that connects all vertices.

* Kruskal and Prim: both greedy algo