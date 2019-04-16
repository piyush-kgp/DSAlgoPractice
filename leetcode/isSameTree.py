# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        P = [p.val]
        Q = [q.val]
        left = p.left
        right = p.right
        while left is not None and right is not None:
            P.append(left.val)
            P.append(right.val)
            left = left.left
