# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    result = []
    max_level = 0
    def zigzag_traversal(self, root, level):
        if not root:
            return
        if level > self.max_level:
            self.result.append([])
            
        self.max_level = max(self.max_level, level)
        self.result[level].append(root.val)
        self.zigzag_traversal(root.left, level+1)
        self.zigzag_traversal(root.right, level+1)
        
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
            if not root:
                return []
            self.result = []
            self.max_level = 0
            self.result.append([])
            self.zigzag_traversal(root, 0)
            return [j[::-1] if i%2 == 1 else j for i, j in enumerate(self.result)]