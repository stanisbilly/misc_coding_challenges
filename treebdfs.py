"""
input.txt:
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

output.txt:
1
2
4
8
9
5
10
11
3
6
12
13
7
14
15

-----
Binary Tree

The task is to build a binary tree using a breadth first insertion method, and
then print out a depth first traversal of the values.

  1. Read in the comma delimited file `input.txt`. We will use these values to
     construct the binary tree.

  2. Build a binary tree using a breadth first insertion method. Your complete
     tree should look like this...


                                    1
                            --------|--------
                            |               |
                            2               3
                        ----|----       ----|----
                        |       |       |       |
                        4       5       6       7
                      --|--   --|--   --|--   --|--
                      |   |   |   |   |   |   |   |
                      8   9  10  11  12  13  14  15


  3. Perform a depth first traversal of the tree printing out one value per
     line.

The output of your solution should match the contents of `output.txt`.
"""

from collections import deque
from enum import Enum

TRAVERSE_MODE = Enum('TRAVERSE_MODE', 'DFS BFS')


def create_node(tree, val, left=None, right=None):
    tree[val] = (left, right)
    return tree


def create_binary_tree(arr):
    arr_len = len(arr)
    tree = {}
    for idx in range(0, arr_len):
        lidx = 2*idx+1
        ridx = 2*idx+2
        leftnode = None if lidx > arr_len - 1 else arr[lidx]
        rightnode = None if ridx > arr_len - 1 else arr[ridx]
        tree = create_node(tree, arr[idx], leftnode, rightnode)
    return tree


def dfs(tree, visited, node):
    if node in tree:
        if node not in visited:
            visited.append(node)
        l, r = tree.get(node)
        if l:
            dfs(tree, visited, l)
        if r:
            dfs(tree, visited, r)
    return visited


def traverse_iter(tree, node, mode=TRAVERSE_MODE.DFS):
    if not tree or not node in tree:
        return []

    # Use deque (double-ended queues) if performing a lot of pop(0).
    # Use popleft() to pop from left-end, pop() to pop from right-end. 
    # Providers higher performance with popping first elements.
    nodes_to_visit = deque([])
    nodes_to_visit.append(node)
    visited = []
    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        if node:
            visited.append(node)
            if node in tree:
                l, r = tree.get(node)
                if mode == TRAVERSE_MODE.BFS:
                    nodes_to_visit.extend([l, r]) # right-most appended first
                else:
                    nodes_to_visit.extendleft([r, l]) # left-most prepended first
    return visited


def run_tests():
    dfs_tests = [
        ([], []),
        ([1], [1]),
        ([1,2,3], [1,2,3]),
        ([1,2,3,4,5,6,7], [1,2,4,5,3,6,7]),
        ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15])
    ]

    for t in dfs_tests:
        tree = create_binary_tree(t[0])
        visited = traverse_iter(tree, 1)
        print(visited == t[1], ', (iterative)', t[0],'-->',visited)
        visited = dfs(tree, [], 1)
        print(visited == t[1], ', (recursive)', t[0],'-->',visited)



if __name__ == '__main__':
    # arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # tree = create_binary_tree(arr)  
    # print('tree:', tree)
    # print('DFS recursive:', dfs(tree, [], 1))
    # print('DFS iterative:', traverse_iter(tree, 1))
    # print('BFS iterative:', traverse_iter(tree, 1, TRAVERSE_MODE.BFS))

    run_tests()