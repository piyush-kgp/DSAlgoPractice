/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if (*root==NULL)
        {
            return NULL;
        }
        int v = root->val;
        if (v>=L && v<=R)
        {
            TreeNode* left = trimBST(root->left, L, R);
            TreeNode* right = trimBST(root->right, L, R);
            root->left = left;
            root->right = right;
            return *root;
        }
        if (left != NULL){
            return *left;
        }
        else{
            return *right;
        }
    }
};
