#!/usr/bin/env python


import unittest

from node import Node


class TestTypecast(unittest.TestCase):

    def print_tree_with_message(self, message):

        print "*"*100
        print message
        self.root.print_tree()
        print "*"*100

    def setUp(self):
        self.root = Node(5)
        self.root.add(Node(4))
        self.root.add(Node(9))
        self.root.add(Node(5))
        self.root.add(Node(7))
        self.root.add(Node(2))
        self.root.add(Node(2))

        # Adding some extra nodes beyond the example for testing
        self.root.add(Node(3))
        self.root.add(Node(8))
        self.root.add(Node(4.5))

    def test_happy_path(self):
        # Nodes are where they should be
        assert self.root.mid.value == 5
        assert self.root.left.value == 4
        assert self.root.left.left.value == 2
        assert self.root.left.left.mid.value == 2
        assert self.root.right.value == 9
        assert self.root.right.left.value == 7

        # Tree has 4 levels
        assert self.root.max_depth() == 4
        self.print_tree_with_message("Happy path tree")

    def test_deleting_mid(self):
        self.root.mid.delete()
        assert self.root.mid is None
        self.print_tree_with_message("Missing the mid 5")

    def test_deleting_leaf(self):
        self.root.right.left.right.delete()
        assert self.root.right.left.right is None
        self.print_tree_with_message("Missing the leaf 8")

    def test_deleting_node(self):
        self.root.left.delete()
        assert self.root.left.value == 2
        self.print_tree_with_message("Rebalanced after losing 4")

    def test_deleting_single_child_node(self):
        self.root.right.left.delete()
        assert self.root.right.left.value == 8
        self.print_tree_with_message("8 shifted up after losing 7")


if __name__ == '__main__':
    unittest.main()
