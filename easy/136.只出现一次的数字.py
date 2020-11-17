# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
#  说明：
#
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#  示例 1:
#
#  输入: [2,2,1]
# 输出: 1
#
#
#  示例 2:
#
#  输入: [4,1,2,1,2]
# 输出: 4
#  Related Topics 位运算 哈希表
#  👍 1584 👎 0

from typing import List
from functools import reduce


# 这个数字与0异或运算以后还是自己， 然后数字与自己运算以后就变成0，  想要
# 不占用额外的空间 就只能使用位运算了， 这个想法简直了，
# a^0 =0 a^a = 0  a^b^a = a^a^b =0^b =b  简直了。

# public int singleNumber(int[] nums) {
#     int single = 0;
#     for (int num : nums) {
#         single ^= num;
#     }
#     return single;
# }

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

# leetcode submit region end(Prohibit modification and deletion)
