# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        q = [];
        if root == None: return [];
        q.append((root, 0));
        ret = [];
        while len(q) > 0:
            tp = q.pop(0);
            cur = tp[0];
            lvl = tp[1];
            if cur.left != None:
                q.append((cur.left, lvl + 1));
            if cur.right != None:
                q.append((cur.right, lvl + 1));
            if len(ret) <= lvl: ret.append([]);
            ret[lvl].append(cur.val);
        return ret;