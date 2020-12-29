class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left:  return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        leftMinDepth  = self.minDepth(root.left)
        rightMinDepth = self.minDepth(root.right)
        return 1 + min(leftMinDepth, rightMinDepth)
