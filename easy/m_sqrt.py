# 实现 int sqrt(int x) 函数。
#
#  计算并返回 x 的平方根，其中 x 是非负整数。
#
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
#  示例 1:
#
#  输入: 4
# 输出: 2
#
#
#  示例 2:
#
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
#
#  Related Topics 数学 二分查找
#  👍 465 👎 0

import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans


# 二分查找法
class Solution1:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
    # leetcode submit region end(Prohibit modification and deletion)


print(True)
