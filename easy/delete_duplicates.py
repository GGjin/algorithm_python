#!/usr/bin/env python
# -*- coding::utf-8 -*-
# Author :GG

# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
#  示例 1:
#
#  输入: 1->1->2
# 输出: 1->2
#
#
#  示例 2:
#
#  输入: 1->1->2->3->3
# 输出: 1->2->3
#  Related Topics 链表
#  👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
# leetcode submit region end(Prohibit modification and deletion)
