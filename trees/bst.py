'''Exercise 2: Implementing Binary Search Trees.'''

from btree import BTree, BTNode


class BST(BTree):
    '''A Binary Search Tree.'''

    def insert(self, value):
        '''Insert a new BTNode with value value into this BST. Do not insert
        duplicates.

        '''

        pass

    def find(self, value):
        '''Return a BTNode from this BST that contains the value value. If
        there is no such BTNode in the tree, raise a
        NoSuchValueException.

        '''

        pass

    def depth(self, value):
        '''Return the depth (the number of BTNodes on the root-to-node path)
        of a BTNode that contains the value value, in this BST. If
        there is no such node in this BST, raise a NoSuchValueException.

        '''

        pass

    def delete(self, value):
        '''Delete a BTNode that contains value value from this BST. If there
        is no such BTNode, raise a NoSuchValueException.

        '''

        # this one will take a bit longer :)
        pass


class NoSuchValueException(Exception):
    pass


if __name__ == '__main__':
    BT = BST(BTNode(5,
                    BTNode(3,
                           BTNode(2, BTNode(1), None),
                           BTNode(4)),
                    BTNode(6, None, BTNode(7))))
    # the string shuld be '\n\t\t7\n\n\t6\n\n5\n\n\t\t4\n\n\t3\n\n\t\t2\n\n\t\t\t1\n'
    print(BT)
    print(BT.preorder())
    print(BT.inorder())
    print(BT.postorder())
    print(BT.is_bst())
    print(BT.size())
    print(BT.fringe())
    print(BT.height())

    print(20*'=')

    for x in (0, 4.5, 10):
        BT.insert(x)
        print(BT)

    print(20*'=')

    for x in (0, 5, 7, 10):
        print('Found {}.'.format(BT.find(x)))

    for x in (-1, 8):
        try:
            BT.find(x)
        except NoSuchValueException:
            print('find({}) raised a NoSuchValueException.'.format(x))

    print(20*'=')

    try:
        BT.find(8)
    except NoSuchValueException:
        print('find(8) raised a NoSuchValueException.')

    for x in (5, 3, 6, 2, 4, 7, 1, 4.5, 10, 0):
        print('Depth of {} is {}.'.format(x, BT.depth(x)))

    try:
        BT.depth(8)
    except NoSuchValueException:
        print('depth(8) raised a NoSuchValueException.')
    print(20*'=')

    try:
        BT.delete(8)
    except NoSuchValueException:
        print('delete(8) raised a NoSuchValueException.')

    for x in (0, 4.5, 10, 5, 2, 3, 7, 4, 6, 1):
        print('Removing {}...'.format(x))
        BT.delete(x)
        print(BT)

    try:
        BT.delete(8)
    except NoSuchValueException:
        print('delete(8) raised a NoSuchValueException.')
