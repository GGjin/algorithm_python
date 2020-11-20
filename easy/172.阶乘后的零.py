# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
#  示例 1:
#
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
#  示例 2:
#
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
#  说明: 你算法的时间复杂度应为 O(log n) 。
#  Related Topics 数学
#  👍 384 👎 0
"""
因为阶乘以后的数太大 容易超出范围，所以考虑问题的时候 最好找到通用的规律， 想知道尾数中零的数量， 可以先思考一下 10是2和5相乘得到的。  然后再 看 2 得到的个数
会比 5得到的个数 多的多，  所以 2不会考虑 最小的问题，只要考虑 其中有多少个可以被5整除的话 就可以得到有多少10相乘了。  然后除了5   5的平方 立方 依次 都包含多个5相乘 需要考虑
比如 n/5  n/25 ...  用循环相加结果就可以
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 0
        while n > 0:
            n //= 5
            num = num + n

        return num

# leetcode submit region end(Prohibit modification and deletion)
