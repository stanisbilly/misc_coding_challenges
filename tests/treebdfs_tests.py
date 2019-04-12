import unittest

from treebdfs import dfs, traverse_iter, create_binary_tree, TRAVERSE_MODE

'''
python -m unittest tests.treebdfs_tests -v
'''

class TestTraversal(unittest.TestCase):

    def dfs_tests(self):
        return [
            ([], []),
            ([1], [1]),
            ([1,2,3], [1,2,3]),
            ([1,2,3,4,5,6,7], [1,2,4,5,3,6,7]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15])            
        ]

    def bfs_tests(self):
        return [
            ([], []),
            ([1], [1]),
            ([1,2,3], [1,2,3]),
            ([1,2,3,4,5,6,7], [1,2,3,4,5,6,7]),
            ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])            
        ]

    def test_bfs_iterative(self):
        for t in self.bfs_tests():
            with self.subTest(t=t):
                tree = create_binary_tree(t[0])
                visited = traverse_iter(tree, 1, TRAVERSE_MODE.BFS)
                self.assertEqual(visited, t[1])

    def test_dfs_iterative(self):
        for t in self.dfs_tests():
            with self.subTest(t=t):
                tree = create_binary_tree(t[0])
                visited = traverse_iter(tree, 1)
                self.assertEqual(visited, t[1])

    def test_dfs_recursive(self):
        for t in self.dfs_tests():
            with self.subTest(t=t):
                tree = create_binary_tree(t[0])
                visited = dfs(tree, [], 1)
                self.assertEqual(visited, t[1])


if __name__ == '__main__':
    unittest.main()