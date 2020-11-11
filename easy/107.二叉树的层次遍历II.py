# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#  例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其自底向上的层次遍历为：
#
#  [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 364 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(root: TreeNode, depth: int):
            if not root:
                return res
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(root.val)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
