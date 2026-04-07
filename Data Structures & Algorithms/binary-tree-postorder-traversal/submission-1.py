# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def Traversal(root):
            if not root:
                return 
            Traversal(root.left)
            Traversal(root.right)
            res.append(root.val)
        Traversal(root)
        return res
