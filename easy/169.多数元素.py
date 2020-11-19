# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法
#  👍 799 👎 0

from typing import List
"""
class Solution {
    public int majorityElement(int[] nums) {
        //1.初始化
        int mode = nums[0];
        int votes = 0;
        //2.遍历
        for(int num : nums){
            if(votes == 0){     //票数是否为0
                mode = num;
            }
            if(num == mode){    //判断当前元素是否为众数
                votes ++;
            }else{
                votes --;
            }
        }
        return mode;   
    }
}

投票算法
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    获取nums数组中指定范围内 某个元素出现的个数
    """

    def count(self, nums: List[int], num: int, l: int, r: int) -> int:
        count = 0
        for i in range(l, r+1):
            if nums[i] == num:
                count += 1
        return count

    def helper(self, nums: List[int], l: int, r: int) -> int:
        if l == r:
            return nums[l]

        mid = (r - l) // 2 + l

        left = self.helper(nums, l, mid)
        right = self.helper(nums, mid + 1, r)

        if left == right:
            return left

        leftCount = self.count(nums, left, l, r)
        rightCount = self.count(nums, right, l, r)

        return left if leftCount > rightCount else right

    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)


# leetcode submit region end(Prohibit modification and deletion)

a = Solution
print(a.majorityElement(a, [7, 7, 7, 2]))
