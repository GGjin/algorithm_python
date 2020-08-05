#!/usr/bin/env python
# -*- coding::utf-8 -*-
# Author :GG

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串
#  👍 1664 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
def isValid(s: str) -> bool:
    map = {")": "(", "}": "{", "]": "["}
    stack = []
    for char in s:
        if char in map:
            top = stack.pop() if stack else "#"
            if top != map[char]:
                return False
        else:
            stack.append(char)

    return not stack

print(isValid("{[]}"))


# leetcode submit region end(Prohibit modification and deletion)
