# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
#  输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
#  示例 1:
#
#  输入: a = "11", b = "1"
# 输出: "100"
#
#  示例 2:
#
#  输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
#  提示：
#
#
#  每个字符串仅由字符 '0' 或 '1' 组成。
#  1 <= a.length, b.length <= 10^4
#  字符串如果不是 "0" ，就都不含前导零。
#
#  Related Topics 数学 字符串
#  👍 445 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        r, p = "", 0
        d = len(a) - len(b)
        a = "0" * -d + a
        b = "0" * d + b

        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return "1" + r if p else r


# leetcode submit region end(Prohibit modification and deletion)

a = Solution1().addBinary("11", "1")

print(a)

print(-2 * "aa")
print(2 * "aa")
