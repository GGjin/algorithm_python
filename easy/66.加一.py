# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组
#  👍 516 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0
        for i in range(0, len(digits)):
            a += digits[i]
            if i != len(digits) - 1:
                a *= 10
        print(f"---${a}")
        a += 1
        return [int(x) for x in str(a)]


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:


        a = 0
        for i in range(0, len(digits)):
            a += digits[i]
            if i != len(digits) - 1:
                a *= 10
        print(f"---${a}")
        a += 1
        return [int(x) for x in str(a)]


# leetcode submit region end(Prohibit modification and deletion)

a = [4, 3, 2, 9]
b = Solution().plusOne(a)

print(b)
