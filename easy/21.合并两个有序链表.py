#!/usr/bin/env python
# -*- coding::utf-8 -*-
# Author :GG

# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
#  示例：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#



# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dump = ListNode(0)
    move = dump
    while l1 and l2:
        if l1.val <= l2.val:
            move.next = l1
            l1 = l1.next
        else:
            move.next = l2
            l2 = l2.next
        move = move.next

    move.next = l1 if l1 else l2
    return dump.next
# leetcode submit region end(Prohibit modification and deletion)
