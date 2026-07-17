# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        L=[]
        def inorder(root):
            if not root:
                return
            root.left=inorder(root.left)
            L.append(root.val)
            root.right=inorder(root.right)
            return root
        inorder(root)
        return L[k-1]
        
