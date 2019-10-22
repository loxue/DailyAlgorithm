# -*- coding:utf-8 -*-
'''
    题目：两两交换链表中的节点
    给定一个链表，两两交换其中相邻的节点，并返回交换后的链表

    示例：
    给定 1->2->3->4,你应该返回2->1->4->3

    说明：
    * 你的算法只能使用常数的额外空间
    * 你不能知识单纯的改变节点内部的值，而是需要实际的进行节点交换

    思路：递归来实现
'''

# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseList(head, k):
            pre = None
            cur = head
            while cur and k > 0:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                k -= 1
            head.next = cur
            return cur, pre
        if not head or not head.next:
            return head
        ret = head.next
        p = head
        pre = None
        while p:
            next, newHead = reverseList(p, 2)
            if pre:
                pre.next = newHead
            pre = p
            p = next
        return ret
