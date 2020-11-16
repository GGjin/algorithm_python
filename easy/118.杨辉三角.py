# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  Related Topics 数组
#  👍 374 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        res = [[1]]

        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res


# leetcode submit region end(Prohibit modification and deletion)


res = [[1, 2, 3, 4]]
new = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
#
# for a in [0] + res[-1]:
#     print(a)
# for a in res[-1] + [0]:
#     print(a)

# for a in res[-1] :
#     print(a)

for a in [0] + [1, 2, 3]:
    print(a)
for a in [1, 2, 3] + [0]:
    print(a)
