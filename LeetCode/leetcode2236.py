from typing import Optional, Callable, Any, Tuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left.val+root.right.val==root.val:
            return True
        else:
            return False

pass

solution=Solution()
root1=TreeNode(4,None,None)
root2=TreeNode(6,None,None)
root0=TreeNode(10,root1,root2)
print(solution.checkTree(root0))