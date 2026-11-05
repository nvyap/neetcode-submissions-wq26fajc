# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        matrix = [[root,1]]
        max_len = 0
        while matrix:
            r,depth = matrix.pop()
            if r:
                max_len = max(max_len,depth)
                matrix.append([r.left,depth+1])
                matrix.append([r.right,depth+1])
        return max_len
        