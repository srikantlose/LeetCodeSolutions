# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        L=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            L.append(root.val)
            inorder(root.right)
            return root
        inorder(root)
        currDiff=0
        minDiff=float('inf')
        for i in range(len(L)-1):
            currDiff=abs(L[i+1]-L[i])
            minDiff=min(minDiff,currDiff)
        return minDiff