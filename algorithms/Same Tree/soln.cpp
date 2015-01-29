/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        //base cases
        if(p == NULL && q == NULL) return true;
        if((p == NULL && q != NULL) || (p != NULL && q == NULL)) return false;
        if(p->val != q->val) return false;
        
        //check structure
        if(p->left == NULL && p->right == NULL && q->left == NULL && q->right == NULL) return true;
        if((p->left == NULL && q->left != NULL) || (p->left != NULL && q->left == NULL)) return false;
        if((p->right == NULL && q->right != NULL) || (p->right != NULL && q->right == NULL)) return false;
        
        //recursive result if structure is the same
        return this->isSameTree(p->left, q->left) && this->isSameTree(p->right, q->right);
    }
};