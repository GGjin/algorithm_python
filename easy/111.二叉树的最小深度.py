# 给定一个二叉树，找出其最小深度。
#
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
#  说明：叶子节点是指没有子节点的节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
#  提示：
#
#
#  树中节点数的范围在 [0, 105] 内
#  -1000 <= Node.val <= 1000
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 399 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        min_depth = 10**5
        if root.left:
            min_depth = min(min_depth, self.minDepth(root.left))
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1
# leetcode submit region end(Prohibit modification and deletion)
