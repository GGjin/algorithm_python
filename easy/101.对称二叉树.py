# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
#
#
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#      1
#    / \
#   2   2
#    \   \
#    3    3
#
#
#
#
#  进阶：
#
#  你可以运用递归和迭代两种方法解决这个问题吗？
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 1105 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

# leetcode submit region end(Prohibit modification and deletion)
