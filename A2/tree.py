
"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""


class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
    """

    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root

    def put(self, node, child):
        """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """
        # TODO implement me. test
        # Node.add_child(node, child) # why did this work?
        node.add_child(child)
        sum = child.key
        node.sum_value += sum
        # use is to check for object's identity not equality to some value
        while node.parent is not None:
            node.parent.sum_value += sum
            node = node.parent

    def flatten(self, node):
        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes including subtree values.

        :param node: The root of the subtree to flatten.

        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)

        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)

        """
        # TODO implement me.

        node.children = []
        node.key = node.sum_value
        node.subtree_value = node.key
        while node.parent != None:
            if node.subtree_value > node.parent.subtree_value:
                node.parent.subtree_value = node.subtree_value
                # node = node.parent causes infinite loop if
                # subtree value is less
            node = node.parent

    def swap(self, subtree_a, subtree_b):
        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """
        # TODO implement me.
        # any changes to parent changes temp
        temp_a = subtree_a.parent
        temp_b = subtree_b.parent
        self.remove(subtree_a)
        self.remove(subtree_b)

        subtree_a.parent = temp_b
        subtree_b.parent = temp_a
        self.put(subtree_a.parent, subtree_a)
        self.put(subtree_b.parent, subtree_b)


    def remove(self, node): #doesn't keep order of children
        if node.parent is not None:
            node.parent.children.remove(node)
            # update subtree_value
            node.parent.subtree_value = node.parent.key
            # check siblings
            for sibling in node.parent.children:
                if sibling.subtree_value > node.parent.subtree_value:
                    node.parent.subtree_value = sibling.subtree_value


        current = node.subtree_value
        sum = node.sum_value

        while node.parent is not None:
            """would this control flow be expressed? no!"""
            # if node.subtree_value > node.parent.subtree_value:
            #     node.parent.subtree_value = node.subtree_value

            # change parent's sub value if their sub value depended on removed
            # node; hidden testcase passed
            if node.subtree_value < node.parent.subtree_value:
                if node.parent.subtree_value == current:
                    node.parent.subtree_value = node.subtree_value
                # node.parent.subtree_value = node.subtree_value

            node.parent.sum_value -= sum
            node = node.parent
