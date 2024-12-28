# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def calHeight(cur):
            if not cur:
                return 0

            leftHeight = calHeight(cur.left)
            rightHeight = calHeight(cur.right)

            self.res = max(self.res, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        
        calHeight(root)

        return self.res
