"""
git add graph.py
git commit -m graph
git push origin master
"""


"""
The polar expedition graph!
===========================

Contains the graph connecting the vertices (or base stations) on the map.

This is going to be the main file that you are modifying. :)

Usage:
    Contains the graph, requires the connection to vertices and edges.
"""
import math

from vertex import Vertex
from edge import Edge


# Define a "edge already exists" exception
# Don't need to modify me.
class EdgeAlreadyExists(Exception):
    """Raised when edge already exists in the graph"""
    def __init__(self, message):
        super().__init__(message)


class Graph:
    """
    Graph Class
    -----------

    Represents the graph of vertices, which is equivalent to the map of base
    stations for our polar expedition.

    Attributes:
        * vertices (list): The list of vertices
    """

    def __init__(self):
        """
        Initialises an empty graph
        """
        self._vertices = []

    def insert_vertex(self, x_pos, y_pos):
        """
        Insert the vertex storing the y_pos and x_pos

        :param x_pos: The x position of the new vertex.
        :param y_pos: The y position of the new vertex.

        :type x_pos: float
        :type y_pos: float

        :return: The new vertex, also stored in the graph.
        """

        v = Vertex(x_pos, y_pos)
        self._vertices.append(v)
        return v

    def insert_edge(self, u, v):
        """
        Inserts the edge between vertex u and v.

        We're going to assume in this assignment that all vertices given to
        this will already exist in the graph.

        :param u: Vertex U
        :param v: Vertex V

        :type u: Vertex
        :type v: Vertex

        :return: The new edge between U and V.
        """

        e = Edge(u, v)

        # Check that the edge doesn't already exist
        for i in u.edges:
            if i == e:
                # Edge already exists.
                raise EdgeAlreadyExists("Edge already exists between vertex!")

        # Add the edge to both nodes.
        u.add_edge(e)
        v.add_edge(e)

    def remove_vertex(self, v):
        """
        Removes the vertex V from the graph.
        :param v:  The pointer to the vertex to remove
        :type v: Vertex
        """

        # Remove it from the list
        del self._vertices[self._vertices.index(v)]

        # Go through and remove all edges from that node.
        while len(v.edges) != 0:
            e = v.edges.pop()
            u = self.opposite(e, v) # want to remove edge from both endpoints
            u.remove_edge(e)

    @staticmethod
    def distance(u, v):
        """
        Get the distance between vertex u and v.

        :param u: A vertex to get the distance between.
        :param v: A vertex to get the distance between.

        :type u: Vertex
        :type v: Vertex
        :return: The Euclidean distance between two vertices.
        """

        # Euclidean Distance
        # sqrt( (x2-x1)^2 + (y2-y1)^2 )

        return math.sqrt(((v.x_pos - u.x_pos)**2) + ((v.y_pos - u.y_pos)**2))

    @staticmethod
    def opposite(e, v):
        """
        Returns the vertex at the other end of v.
        :param e: The edge to get the other node.
        :param v: Vertex on the edge.
        :return: Vertex at the end of the edge, or None if error.
        """

        # It must be a vertex on the edge.
        if v not in (e.u, e.v):
            return None

        if v == e.u:
            return e.v

        return e.u

    ##############################################
    # Implement the functions below
    ##############################################

    def find_emergency_range(self, v):
        """
        Returns the distance to the vertex W that is furthest from V.
        :param v: The vertex to start at.
        :return: The distance of the vertex W furthest away from V.
        """
        # return 0
        if v not in self._vertices:
            return 0
        # TODO implement me!
        current_max = 0 # 0
        if len(self._vertices) <= 1:
            return 0 # had to return 0 instead of return
        for u in self._vertices:
            if u != v:
                dist = self.distance(u, v)
                if dist > current_max:
                    current_max = dist
        return current_max

    """ Helper functions DFS and DFS_visit """

    def DFS_visit(self, u, goal, visited, current_path, all_paths):
        visited.append(u)
        current_path.append(u)

        if u == goal:
            cp_tuple = tuple(current_path)
            all_paths.append(cp_tuple)

        else:
            # visit neighbours of u
            for e in u.edges:
                v = self.opposite(e, u)
                if v not in visited:
                    self.DFS_visit(v, goal, visited, current_path, all_paths)

        current_path.pop()
        visited.remove(u)


    def DFS(self, b, s):
        visited = []
        current_path = []
        all_paths = []

        self.DFS_visit(b, s, visited, current_path, all_paths)

        # clear ?
        visited = []
        current_path = []

        return all_paths



    def find_path(self, b, s, r):
        """
        Find a path from vertex B to vertex S, such that the distance from B to
        every vertex in the path is within R.  If there is no path between B
        and S within R, then return None.

        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :param r: The maximum range of the radio.
        :return: The LIST of the VERTICES in the path.
        """
        # TODO implement me!
        # return None
        if b not in self._vertices or s not in self._vertices:
            return None
        # find possible paths, disregarding r
        all_paths = self.DFS(b, s)
        if len(all_paths) == 0:
            return None

        if b == s:
            return [b]

        # now return a path that is within r
        found = 0
        i = 0
        for path in all_paths:
            # assume each path is right initially
            match = 1
            for u in path:
                dist = self.distance(u, b)
                # update match if outside range
                if dist > r:
                    match = 0
            if match == 1:
                found = 1
                break
            i += 1

        if found == 0:
            return None

        # clear all paths
        result = all_paths[i]
        all_paths = []

        return result

    def minimum_range(self, b, s):
        """
        Returns the minimum range required to go from Vertex B to Vertex S.
        :param b: Vertex B to start from.
        :param s: Vertex S to finish at.
        :return: The minimum range in the path to go from B to S.
        """
        # return -1
        # TODO implement me!
        if b not in self._vertices or s not in self._vertices:
            return 0
        if len(self._vertices) <= 1:
            return 0

        all_paths = self.DFS(b, s)
        if len(all_paths) == 0:
            return 0

        max_list = []

        # if b and s is the same?
        # if b == s:
        #     return 0
        # print(all_paths, len(all_paths))

        for path in all_paths:
            current_max = -1 # appending -1
            for u in path:
                if u != b:
                    dist = self.distance(u, b)
                else:
                    dist = 0
                if dist > current_max:
                    current_max = dist

            max_list.append(current_max)
        min_range = min(max_list)

        if b == s:
            return 0


        # res = []
        # i = 0
        # while i < len(self._vertices):
        #     # if self._vertices[i] != b:
        #     res.append(self.distance(self._vertices[i], b))
        #     i += 1
        # return res[11]


        # clear paths
        all_paths = []
        max_list = []

        return min_range

    def move_vertex(self, v, new_x, new_y):
        """
        Move the defined vertex.

        If there is already a vertex there, do nothing.

        :param v: The vertex to move
        :param new_x: The new X position
        :param new_y: The new Y position
        """
        # TODO implement me!
        for u in self._vertices:
            if u.x_pos == new_x and u.y_pos == new_y:
                return
        v.move_vertex(new_x, new_y)

# G = Graph()
#
# # Layer 1
# A = G.insert_vertex(0, 0)
#
# # Layer 2
# B = G.insert_vertex(2, 0)
# C = G.insert_vertex(2, 98)
# D = G.insert_vertex(2, 99)
#
# # Layer 3
# E = G.insert_vertex(3, 3)
# F = G.insert_vertex(4, 6)
#
# # Make the edges
# G.insert_edge(A, B)
# G.insert_edge(A, C)
# G.insert_edge(A, D)
# G.insert_edge(C, E)
# G.insert_edge(C, F)
# G.insert_edge(D, F)
#
# # Find the minimum range
#
# r = G.minimum_range(A, A)
# print(r)
