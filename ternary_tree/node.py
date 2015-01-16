#!/usr/bin/env python


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.mid = None
        self.right = None
        self.parent = None

    def add(self, node):
        """
            Entry pont for adding a node object to a tree. This method figures
            out which branch they belong on, and then sends it off to the
        """

        if self.value < node.value:
            side = "right"
        elif self.value > node.value:
            side = "left"
        elif self.value == node.value:
            side = "mid"

        # Once we know where it goes, see if the slot is full. If it is, call
        # that nodes add. This goes on until we find an empty slot
        if getattr(self, side):
            getattr(self, side).add(node)
        else:
            node.parent = self
            setattr(self, side, node)

    def _depth_of_side(self, side):
        """
            Instead of adding a depth method onto the child, ie self.left.depth
            this method allows you to do self._depth_of_side("left"). This is
            important so that you can check the depth of a side, even if there
            are no nodes on that side, depth is simply 0
        """
        if getattr(self, side):
            return getattr(self, side).max_depth()
        else:
            return 0

    def max_depth(self):
        """
            This looks circular with _depth_of_side, but this calls that method
            for 3 children nodes, and grabs the deepest of those.
        """
        return max(self._depth_of_side("left"),
                   self._depth_of_side("mid"),
                   self._depth_of_side("right")) + 1

    def delete(self):
        """
            Remove a node, rebalancing children if necessary. There is no need
            to delete the object as python will GC this once all references to
            it are out of scope.
        """
        # Figure out where on the parent we are so we can reset it
        if self.parent.value > self.value:
            parent_side = "left"
        elif self.parent.value < self.value:
            parent_side = "right"
        else:
            parent_side = "mid"

        # It's a leaf node. Just delete it from the parent. This one's easy
        if self.max_depth() == 1:
            setattr(self.parent, parent_side, None)

        # If it has a mid, just shift it mid up. A mid can't have left/right
        # children to rebalance, so it becomes simple
        elif self.mid:
            setattr(self.parent, parent_side, self.mid)
            if self.left:
                self.left.parent = self.mid

            if self.right:
                self.right.parent = self.mid

            self.mid.parent = self.parent
            self.mid.left = self.left
            self.mid.right = self.right

        # We have to pick a side now. If we can, pick the deepest, otherwise
        # we have to just pick one. It could be random, but for consistency
        # and repeatability we'll just pick the left side. If we decide to add
        # more rules/logic, it's trivial to add to the else statement
        elif self._depth_of_side("right") > self._depth_of_side("left"):

            setattr(self.parent, parent_side, self.right)
            self.right.parent = self.parent
            if self.left:
                self.right.add(self.left)
        else:
            setattr(self.parent, parent_side, self.left)
            self.left.parent = self.parent
            if self.right:
                self.left.add(self.right)

    def print_tree(self):
        """
            Try to show a reasonable representation of the tree in the
            terminal. Essentially, we're going top to bottom, left to right and
            adding things onto a temporary dict. It is easier to display it
            all at once.
        """

        def render_node(node, total_depth=0, current_level=1, output=None):
            """
                The nasty recursive part of the show logic. Here be dragons
                and magic numbers in order to get spacing to be (mostly) sane.
            """

            if output is None:
                output = {}

            if total_depth == 0:
                total_depth = node.max_depth()

            max_leaf_nodes = pow((total_depth+2) - current_level, 3)
            line_length = max_leaf_nodes / 2

            if output.get(current_level, None) is None:
                output[current_level] = ""

            output[current_level] += " " * (line_length)

            if node:
                output[current_level] += str(node.value)
            else:
                output[current_level] += " "

            if node:
                render_node(node.left, total_depth, current_level+1, output)
                render_node(node.mid, total_depth, current_level+1, output)
                render_node(node.right, total_depth, current_level+1, output)

            # Even if there is no node, we need it to render for the spaces
            elif total_depth > current_level:
                render_node(None, total_depth, current_level+1, output)
                render_node(None, total_depth, current_level+1, output)
                render_node(None, total_depth, current_level+1, output)

            return output

        output = render_node(self)

        for key, line in output.iteritems():
            print line
            print
