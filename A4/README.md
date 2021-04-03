# Assignment 4 - Polar Expedition

## Information about the graph

Every Vertex has an X and Y coordinate indicating its location.

The graph is NOT necessarily complete, but you can assume that it is connected. 


## Code

### vertex.py

* ``move_vertex(self, x_pos, y_pos)`` - Move the position of the vertex to the defined x and y provided as arguments.


### graph.py

* ``find_emergency_range(self, v)`` - Find the distance to the vertex w that is furthest away from v.
* ``find_path(self, b, s, r)`` - Find a path from the vertex b to vertex s such that the distance from b to every vertex along this path is within range r. 
* ``minimum_range(self, b, s)`` - Return the minimum range required to go from b to s.
* ``move_vertex(self, v, new_x, new_y)`` - Move vertex v to the new x and y positions provided.


## About the code

### Vertex Class - vertex.py

**Attributes**:

* ``x_pos`` - x position of the vertex
* ``y_pos`` - y position of the vertex
* ``edges`` - set of edges that are linked to this vertex.

**Functions**: 

* ``init(x_pos, y_pos)`` - initialises the x and y position of the vertex.
* ``add_edge(e)`` - adds the edge to the vertex.
* ``remove_edge(e)`` - removes the edge from the vertex.
* ``move_vertex(x_pos, y_pos)`` - moves the position of the vertex to the new x and y. 

### Edge Class - edge.py

**Attributes**:

* `u` - A vertex connected with this edge.
* `v` - A vertex connected with this edge.


### Graph Class - graph.py

**Attributes**:

* ``_vertices`` - List of the vertices contained in the graph.

**Functions**:

* ``insert_vertex(x_pos, y_pos)`` - Creates, stores and returns a new vertex at the provided x and y coordinates.
* ``insert_edge(u, v)`` - Creates and returns a new edge between vertex u and vertex v.\
* ``remove_vertex(v)`` - Removes the vertex v from the graph.
* ``distance(u, v)`` - Returns the Euclidian distance between vertex u and vertex v. 
* ``find_emergency_range(v)`` - Returns the distance to the vertex v that is furthest from v.
* ``find_path(b, s, r)`` - Returns a path from b to s, such that all vertices in the path are within range r from b. 
* ``minimum_range(b, s)`` - Returns the minimum range required to go from b to s. 
* ``move_vertex(v, new_x, new_y)`` - Moves vertex v to the coordinates provided by new_x and new_y. 


