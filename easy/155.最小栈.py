# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
#
#  push(x) —— 将元素 x 推入栈中。
#  pop() —— 删除栈顶的元素。
#  top() —— 获取栈顶元素。
#  getMin() —— 检索栈中的最小元素。
#
#
#
#
#  示例:
#
#  输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
#
#
#  提示：
#
#
#  pop、top 和 getMin 操作总是在 非空栈 上调用。
#
#  Related Topics 栈 设计
#  👍 731 👎 0

import math


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
"""
在要求不需要额外空间的情况下，可以在栈中保存与最小值的差值来不使用额外空间
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_num = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_num = x
        else:
            diff = x - self.min_num
            self.stack.append(diff)
            self.min_num = self.min_num if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_num
                self.min_num = self.min_num - diff
            else:
                top = self.min_num + diff
            return top
        else:
            return self.min_num

    def top(self) -> int:
        return self.min_num if self.stack[-1] < 0 else self.stack[-1] + self.min_num

    def getMin(self) -> int:
        return self.min_num
