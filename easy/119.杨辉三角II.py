# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 3
# 输出: [1,3,3,1]
#
#
#  进阶：
#
#  你可以优化你的算法到 O(k) 空间复杂度吗？
#  Related Topics 数组
#  👍 197 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return []
        res = [[1]]
        while len(res[-1]) <= rowIndex:
            newRow = [a + b for a, b in zip(res[-1] + [0], [0] + res[-1])]
            res = [newRow]
        return res[-1]
# leetcode submit region end(Prohibit modification and deletion)
