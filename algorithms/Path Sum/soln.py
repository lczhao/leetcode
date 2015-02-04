# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return hasPathSum_h(root,sum);
def hasPathSum_h(root, sum):
    if root == None: return False;
    if root.left == None and root.right == None:
        return root.val == sum;
    if root.left == None:
        return hasPathSum_h(root.right, sum - root.val);
    elif root.right == None:
        return hasPathSum_h(root.left, sum-root.val);
    else:
        return (hasPathSum_h(root.right, sum - root.val) or hasPathSum_h(root.left, sum-root.val));