# 编写一个函数来查找字符串数组中的最长公共前缀。
#
#  如果不存在公共前缀，返回空字符串 ""。
#
#  示例 1:
#
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
#  示例 2:
#
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
#  说明:
#
#  所有输入只包含小写字母 a-z 。
#  Related Topics 字符串
#  👍 1136 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0: return ""
    res = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(res) != 0:
            res = res[0:len(res) - 1]
        if len(res) == 0:
            break

    return res
# leetcode submit region end(Prohibit modification and deletion)
