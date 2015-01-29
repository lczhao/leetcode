# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        s = self.flatTree(root, 0);
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False;
        return True;
        
    def flatTree(self, root, level):
        if root == None:
            return [];
        left = self.flatTree(root.left, level + 1);
        right = self.flatTree(root.right, level + 1);
        
        return left + [(root.val, level)] + right;