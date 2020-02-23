'''Exercise 1: Implementing Binary Trees.'''


class BTree:
    '''A Binary Tree.'''

    def __init__(self, node=None):
        '''Init a BTree rooted at node.'''

        self._root = node

    def is_bst(self):
        '''Return True iff this BTree is a binary search tree.  Use < for node
        comparison.

        '''

        return _is_bst(self._root)

    def preorder(self):
        '''Return a list of values in this BTree, corresponding to a pre-order
        traversal.

        '''

        pass

    def inorder(self):
        '''Return a list of values in this BTree, corresponding to an in-order
        traversal.

        '''

        pass

    def postorder(self):
        '''Return a list of values in this BTree, corresponding to a
        post-order traversal.

        '''

        pass

    def size(self):
        '''Return the number of nodes in this BTree.'''

        pass

    def height(self):
        '''Return the height of this BTree: the number of nodes on the longest
        root-to-leaf path.

        '''

        pass

    def fringe(self):
        '''Return a list of leaves in this BTree, in left-to-right order.'''

        pass

    def __str__(self):
        '''Return a str representation of this BTree.'''

        pass


class BTNode:
    '''A node in a BTree.'''

    def __init__(self, value, left=None, right=None):
        '''Init a BTNode with value value, left child left, and right child
        right.

        '''

        self.value = value
        self.left = left
        self.right = right

    def __lt__(self, other):
        '''Return whether the value in this BTNode is less than the value in
        BTNode other.

        '''

        return self.value < other.value

    def __eq__(self, other):
        '''Return whether the value in this BTNode is equal the value in
        BTNode other.

        '''

        return self.value == other.value

    def __str__(self):
        '''Return a str representation of a tree rooted in this BTnode.'''

        return _str(self)


def _preorder(node):
    '''Return a list of values in a BTree rooted at node, corresponding to
    a pre-order traversal.

    '''

    pass


def _inorder(node):
    '''Return a list of values in a BTree rooted at node, corresponding to
    a in-order traversal.

    '''

    pass


def _postorder(node):
    '''Return a list of values in a BTree rooted at node, corresponding to
    a post-order traversal.

    '''

    pass


def _str(node, offset=0):
    '''Return a str representation of a BTree rooted at node.'''

    pass


def _is_bst(node):
    '''Return True iff the BTree rooted at node is a binary search tree.
    Use Python's < for node comparison.

    '''

    pass


def _size(node):
    '''Return the number of nodes in the BTree rooted at node.'''

    pass


def _fringe(node):
    '''Return a list of leaves in the BTree rooted at node, in
    left-to-right order.

    '''

    pass


def _height(node):
    '''Return the height of the BTree rooted at node: the number of nodes
    on the longest root-to-leaf path.

    '''

    pass


if __name__ == '__main__':
    BT = BTree(BTNode(5,
                      BTNode(3,
                             BTNode(2, BTNode(1), None),
                             BTNode(4)),
                      BTNode(6, None, BTNode(7))))
    BT2 = BTree(BTNode(5,
                       BTNode(3,
                              BTNode(2, BTNode(3), None),
                              BTNode(4)),
                       BTNode(6, None, BTNode(7))))
    # the string shuld be '\n\t\t7\n\n\t6\n\n5\n\n\t\t4\n\n\t3\n\n\t\t2\n\n\t\t\t1\n'
    print(BT)
    print(BT.preorder())
    print(BT.inorder())
    print(BT.postorder())
    print(BT.is_bst())
    print(BT2.is_bst())
    print(BT.size())
    print(BT.fringe())
    print(BT.height())
