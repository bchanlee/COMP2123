"""
Simple test cases
-----------------

Use this file for simple example tests, this shows basic functionality which
should get you passing some of the tests.

To run this, in the main directory run:

python -m unittest tests/test_simple_functions.py

"""
import unittest

import node
import tree


class SimpleFunctionsTestCase(unittest.TestCase):
    """
    Simple sample tests that can be used to test your implementation
    before your submission.
    """

    def setUp(self):
        root = node.Node(5, None)
        self.tree = tree.Tree(root)

    def test_can_insert_single(self):
        """
        Inserts a single node into the tree.

        r
        |
        A
        """
        new_node = node.Node(10, self.tree.root)
        self.tree.put(self.tree.root, new_node)

        # Check
        assert len(self.tree.root.children) == 1, \
            "expected: {}, got: {}".format(1, len(self.tree.root.children))
        assert self.tree.root.subtree_value == 10, \
            "expected: {}, got: {}".format(10, self.tree.root.subtree_value)

    def test_can_insert_two(self):
        """
        Makes a simple tree.
        r
        | \
        A  B
        """
        node_a = node.Node(10, self.tree.root)
        node_b = node.Node(8, self.tree.root)
        self.tree.put(self.tree.root, node_a)

        # Check
        assert len(self.tree.root.children) == 1, \
            "expected: {}, got: {}".format(1, len(self.tree.root.children))
        assert self.tree.root.subtree_value == 10, \
            "expected: {}, got: {}".format(10, self.tree.root.subtree_value)

        self.tree.put(self.tree.root, node_b)

        assert len(self.tree.root.children) == 2, \
            "expected: {}, got: {}".format(2, len(self.tree.root.children))
        assert self.tree.root.subtree_value == 10, \
            "expected: {}, got: {}".format(10, self.tree.root.subtree_value)

    def test_bubble_up_value(self):
        """
        Addition of third level, should bubble up the values

        root
        |  \
        A  B
        |
        C
        |
        D
        """
        root = self.tree.root
        node_a = node.Node(4, self.tree.root)
        node_b = node.Node(5, self.tree.root)
        node_c = node.Node(6, node_a)
        node_d = node.Node(8, node_c)

        self.tree.put(root, node_a)
        self.tree.put(root, node_b)
        assert len(self.tree.root.children) == 2, \
            "expected: {}, got: {}".format(2, len(self.tree.root.children))
        assert self.tree.root.subtree_value == 5, \
            "expected: {}, got: {}".format(5, self.tree.root.subtree_value)
        self.tree.put(node_a, node_c)
        assert self.tree.root.subtree_value == 6, \
            "expected: {}, got: {}".format(6, self.tree.root.subtree_value)
        assert node_a.subtree_value == 6, \
            "expected: {}, got: {}".format(6, node_a.subtree_value)

        self.tree.put(node_c, node_d)

        assert self.tree.root.subtree_value == 8, \
            "expected: {}, got: {}".format(8, self.tree.root.subtree_value)
        assert node_a.subtree_value == 8, \
            "expected: {}, got: {}".format(8, node_a.subtree_value)

    def test_simple_flatten(self):
        """
        Simple flatten
        (Shouldn't do anything)
        A       A
        |   >   |
        B       B
        """

        root = self.tree.root
        node_a = node.Node(4, self.tree.root)

        self.tree.put(root, node_a)

        self.tree.flatten(node_a)

        assert node_a.key == 4, "expected: {}, got: {}".format(4, node_a.key)
        assert node_a.is_external(), "Node should be leaf after flattening."

    def test_simple_flatten_merge(self):
        """
        Flatten should merge

          r         r
        / |    >  /  |
        A  B     A  B_NEW
         / |
        C  D
        """

        root = self.tree.root
        node_a = node.Node(4, self.tree.root)
        node_b = node.Node(5, self.tree.root)

        node_c = node.Node(5, node_b)
        node_d = node.Node(59, node_b)

        self.tree.put(root, node_a)
        self.tree.put(root, node_b)
        self.tree.put(node_b, node_c)
        self.tree.put(node_b, node_d)

        self.tree.flatten(node_b)

        # It should be a leaf.
        assert len(node_b.children) == 0, \
            "expected: {}, got: {}".format(0, len(node_b.children))
        assert node_b.is_external(), "Node should be leaf after flattening."

        # The node key should be the sum of the children.
        assert node_b.key == 69, "expected: {}, got {}".format(69, node_b.key)

    def test_example_swap(self):
        """
        Can perform swap as shown in example

           A(5)
           / \
         C(2) D(8)
          |
         B(10)

         > tree.swap(B, D)

           A(5)
           / \
         C(2) B(10)
          |
         D(8)

        """

        root = self.tree.root
        C = node.Node(2, root)
        B = node.Node(10, root)
        D = node.Node(8, C)

        self.tree.put(root, B) # subtree 10 @ root
        self.tree.put(root, C) # subtree 10 @ root
        self.tree.put(C, D) # subtree 8 @ root

        assert C.subtree_value == 8, \
            "expected: {}, got: {}".format(8, C.subtree_value)
        assert root.subtree_value == 10, \
            "expected: {}, got: {}".format(10, root.subtree_value)

        self.tree.swap(B, D)

        assert C.subtree_value == 10, \
            "expected: {}, got: {}".format(10, C.subtree_value)
        assert root.subtree_value == 10, \
            "expected: {}, got: {}".format(10, root.subtree_value)

    def test_simple_swap(self):
        """
        Swap subtree A and B correctly.

                root
              /  |   \
             A   B    C
           /  |      / \
          D   E     G   H
             /
            F

        swap(A, C)

                root
              /  |   \
             C   B    A
           /  |      / \
          G   H     D   E
                       /
                      F

        swap(F, C)

                root
              /  |   \
             F   B    A
                     / \
                    D   E
                       /
                      C
                    /  \
                   G    H
        """

        # Generate the nodes
        root = self.tree.root
        node_a = node.Node(4, self.tree.root)
        node_b = node.Node(5, self.tree.root)
        node_c = node.Node(6, self.tree.root)
        node_d = node.Node(7, node_a)
        node_e = node.Node(8, node_a)
        node_f = node.Node(9, node_e)
        node_g = node.Node(10, node_c)
        node_h = node.Node(11, node_c)

        # Put them into the tree.
        self.tree.put(root, node_a)
        self.tree.put(root, node_b)
        self.tree.put(root, node_c)
        self.tree.put(node_a, node_d)
        self.tree.put(node_a, node_e)
        self.tree.put(node_e, node_f)
        self.tree.put(node_c, node_g)
        self.tree.put(node_c, node_h)

        # Check that the values are correct
        assert root.subtree_value == 11, \
            "expected: {}, got: {}".format(11, root.subtree_value)
        assert node_c.subtree_value == 11, \
            "expected: {}, got: {}".format(11, node_c.subtree_value)
        assert node_a.subtree_value == 9, \
            "expected: {}, got: {}".format(9, node_a.subtree_value)

        # Let's get swapping!
        # ezmode
        self.tree.swap(node_a, node_c)

        assert root.subtree_value == 11, \
            "expected: {}, got: {}".format(11, root.subtree_value)
        assert node_c.subtree_value == 11, \
            "expected: {}, got: {}".format(11, node_c.subtree_value)
        assert node_a.subtree_value == 9, \
            "expected: {}, got: {}".format(9, node_a.subtree_value)

        assert node_c.parent == root
        assert node_a.parent == root

        assert len(node_c.children) == 2
        assert len(node_a.children) == 2

        # ??\_(???)_/??
        self.tree.swap(node_f, node_c)

        # Root value should stay
        assert self.tree.root.subtree_value == 11

        # Parent and children should have swapped
        # correctly
        assert node_f.parent == root, "Node should swap parent."
        assert node_c.parent == node_e, "Node should swap parent."
        assert node_c in node_e.children, "Node should add children."

        # Values should be propagated.
        # subtree_values should look like:
        #         11
        #      /  |   \
        #     9  5    11
        #             / \
        #            7   11
        #               /
        #              11
        #            /  \
        #           10   11

        assert node_f.subtree_value == 9, \
            "expected: {}, got: {}".format(9, node_f.subtree_value)

        for i in [node_a, node_e, node_c]:
            assert i.subtree_value == 11, \
                "expected: {}, got: {}".format(11, i.subtree_value)

        assert node_d.subtree_value == 7, \
            "expected: {}, got: {}".format(7, node_d.subtree_value)

    def test_my_swap(self):
        """
        Can perform swap as shown in example


          100
        /      \
       100      10
     /  |      / \
    50   100  2  10

         > tree.swap(100, 10) on bottom row



        """

        root = self.tree.root
        A = node.Node(1, root)
        B = node.Node(50, A)
        C = node.Node(100, A)
        D = node.Node(3, root)
        E = node.Node(2, D)
        F = node.Node(10, D)

        self.tree.put(root, A) # subtree 10 @ root
        self.tree.put(root, D) # subtree 10 @ root
        self.tree.put(A, B) # subtree 8 @ root
        self.tree.put(A, C) # subtree 8 @ root
        self.tree.put(D, E) # subtree 8 @ root
        self.tree.put(D, F) # subtree 8 @ root


        assert root.subtree_value == 100, \
            "expected: {}, got: {}".format(100, root.subtree_value)

        self.tree.swap(C, E)

        assert A.subtree_value == 50, \
            "expected: {}, got: {}".format(50, A.subtree_value)
        assert D.subtree_value == 100, \
            "expected: {}, got: {}".format(100, D.subtree_value)


if __name__ == '__main__':
    unittest.main()
