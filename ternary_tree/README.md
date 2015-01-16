
## Ternary Tree

### Objective
Implement insert and delete in a ternary tree.

### Overview
A [Ternary Tree](http://en.wikipedia.org/wiki/Ternary_tree) is a data structure
similar to a binary tree, where each node is able to have up to three children
(as opposed to a maximum of two in a binary tree). This data structure gives you
nearly all of the power of a binary tree, as well as the capability to have
duplicate (matching) entries.

### Solution
There are two core components in this: insert and delete.

#### Inserting
The tree starts with a root node. Once a root node is created, additional nodes
can be created and inserted to the tree. When a node is inserted, the process
begins with the root node. Through a series of value checks, the node eventually
finds a vacant spot to rest. Once the node is in its position, it is then used
for further nodes to attach to. For this reason, the order elements are added
to the node is very important to the structure.

#### Deleting
The second piece of puzzle is the removal of nodes. All nodes are handled in
one of three ways

A leaf node is a node with no attached children. The only reference a leaf node
has is the parent to leaf and leaf to parent. Deleting leaf nodes is simply a
matter of removing those 2 references.

An mid is a node that has the same value as the parent. When a node with a mid
is deleted, the mid can be pushed up the stack, resulting in no rebalancing.
Since the values are the same, the mid just replaces the parent.

The last case unfortunately requires all children nodes to be rebalanced. If we
have gotten this far, it does not have a mid, but does have left and/or right
children. My solution checks to see which side should be pushed up higher in the
tree, and then re-adds the top node of the opposite side of the tree to itself.

### Examples

Example of a simple ternary tree
```
       5
     / | \
    4  5   9
  /       /
 2      7
 |
 2
```

Inserting an 8 onto this tree would be 3 evaluations.
- 8 is greater than 5, so move right.
- 8 is less than 9, so move left.
- 8 is greater than 7, move right.
- The spot on 7's right is open, so end there.
```
       5        Becomes          5
     / | \                     / | \
    4  5   9                  4  5   9
  /       /                 /       /
 2      7                  2      7
 |                         |       \
 2                         2         8
```


Deleting the Leaf node 2 is a simple parent/child modification
```
       5        Becomes          5
     / | \                     / | \
    4  5   9                  4  5   9
  /       /                 /       /
 2      7                  2      7
 |
 2
```

Deleting the root element 5 is actually a very simple operation. The only
references updated are the 4 and 9 parent, and the 5s left/right
```
       5        Becomes          5
     / | \                     /   \
    4  5   9                  4      9
  /       /                 /       /
 2      7                  2      7
 |                         |
 2                         2
```


Deleting the 4 requires elements to shift, and depending on the depth of the tree
may result in a significant decrease in efficiency.
```
       7        Becomes          7
     /   \                     /   \
    4      9                  2      9
  /  \                        | \
 2     5                      2  3
 | \    \                     |   \
 2  3    6                    2    5
 |                                  \
 2                                   6
```
