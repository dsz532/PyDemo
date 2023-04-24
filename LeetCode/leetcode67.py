from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        selected = root
        if selected.left != None:
            mid = TreeNode(-1, selected.left, None)
            selected.left=mid
            self.expandBinaryTree(mid.left)
        selected = root
        if selected.right != None:
            mid = TreeNode(-1, None, selected.right)
            selected.right=mid
            self.expandBinaryTree(mid.right)
        return root
pass
sol=Solution()
left=TreeNode(5,None,None)
right=TreeNode(6,None,None)
root=TreeNode(7,left,right)
sol.expandBinaryTree(root)