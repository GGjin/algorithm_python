# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
#  例如，
#
#      1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
#
#
#  示例 1:
#
#  输入: 1
# 输出: "A"
#
#
#  示例 2:
#
#  输入: 28
# 输出: "AB"
#
#
#  示例 3:
#
#  输入: 701
# 输出: "ZY"
#
#  Related Topics 数学
#  👍 288 👎 0

"""
chr 可以直接转为chr类型， 这样能直接转为 大写字母  A是 65   这道题是 一个10进制转为26进制的问题，但是需要注意的是 这个到了26的时候不会进位，
相当于范围是1-26 而不是正常的0-25  需要注意的就是这点
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, n: int) -> str:
        return "" if not n else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + 65)


# leetcode submit region end(Prohibit modification and deletion)


a = Solution

print(a.convertToTitle(a, 702))
