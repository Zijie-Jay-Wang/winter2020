'''Exercise 3. Complexity of tree operations -- Part 1.'''

import random
import statistics
import matplotlib.pyplot as plt

from bst import BST
from btree import BTNode, BTree


def get_random_btree(items: list):
    '''Return a BTree with elements from items inserted at random:
    all insertions at leaf level;
    at each level, go right with prob 50% and left with prob 50%.'''

    pass


def random_insert(node, value):
    '''Return node with value insterted randomly into a subtree rooted at node;
    insertion at leaf level;
    at each level, go right with prob 50% and left with prob 50%.'''

    # use random.random() to decide left or right

    pass


def get_bst(items):
    '''Return a BST with elements from items, inserted in order starting
    with an empty tree.

    '''

    pass


def get_random_bst(num_nodes):
    '''Return a BST created by inserting elements from range(num_nodes) in
    random order.'''

    # use random.shuffle() to randomize a list

    pass


def plot_heights_bsts(num_nodes, num_trees):
    '''For each N in range(num_nodes), create num_trees random BSTs of size
    N, and calculate their average height. Return a list
    [avg_height_0, avg_height_1, ..., avg_height_N-1]
    '''

    # use statistics.mean() to calculate the averages

    pass


def plot_heights_btrees(num_nodes, num_trees):
    '''For each N in range(num_nodes), create num_trees random BTrees of
    elements [0,..N), and calculate their average height. Return a list
    [avg_height_0, avg_height_1, ..., avg_height_N-1]
    '''

    # use statistics.mean() to calculate the averages

    pass


if __name__ == '__main__':

    # Plot num_nodes vs average height of random BST with num_nodes nodes.
    NUM_TREES = 50
    MAX_NODES = 1000

    XS = list(range(MAX_NODES))

    '''
    YS1 = plot_heights_btrees(MAX_NODES, NUM_TREES)
    YS2 = plot_heights_bsts(MAX_NODES, NUM_TREES)

    plt.xlabel('Number of nodes.')
    plt.ylabel('Average height.')
    plt.plot(XS, YS1, label='randomly built binary trees')
    plt.plot(XS, YS2, label='random bsts')
    plt.legend()

    plt.show()
    '''
