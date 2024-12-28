# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calHeight(cur):
            if not cur:
                return 0
            else:
                return 1 + max(calHeight(cur.left), calHeight(cur.right))
        if calHeight(root) <= 1:
            return True
        leftHeight = calHeight(root.left)
        rightHeight = calHeight(root.right)

        return (abs(leftHeight - rightHeight) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right)