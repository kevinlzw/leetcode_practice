# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_num = float('-inf')

    def highestSum(self, root):
        if not root:
            return 0
        return max(self.highestSum(root.left), self.highestSum(root.right)) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = self.highestSum(root.left) + self.highestSum(root.right) + root.val
        self.max_num = max(self.max_num, res)
        self.maxPathSum(root.left)
        self.maxPathSum(root.right)
        return self.max_num