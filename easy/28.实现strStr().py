#!/usr/bin/env python
# -*- coding::utf-8 -*-
# Author :GG

# 实现 strStr() 函数。
#
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。
#
#  示例 1:
#
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
#  示例 2:
#
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
#  说明:
#
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#  Related Topics 双指针 字符串
#  👍 496 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        try:
            return haystack.index(needle)
        except(ValueError):
            return -1

    def strstr2(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        l1 = len(haystack)
        l2 = len(needle)
        if l1 < l2: return -1
        for i in range(0, l1 - l2 + 1):
            k = i
            j = 0
            while j < l2 and k < l1 and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == l2:
                return i

        return -1


# leetcode submit region end(Prohibit modification and deletion)

a = Solution()
b = a.strstr2("a", "a")
print(b)
