# -*- coding:utf-8 -*-
'''
    题目：给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
         k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
         那么将最后剩余节点保持原有顺序。

    示例 :
    给定这个链表： 1->2->3->4->5
    当 k = 2 时，应当返回: 2->1->4->3->5
    当 k = 3 时，应当返回: 3->2->1->4->5

    说明 :
    你的算法只能使用常数的额外空间。
    你不能只是单纯的改变节点内部的值 ，而是需要实际的进行节点交换。

    思路：栈或者递归

'''

# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        '''
        :type head:ListNode
        :type k:int
        :rtype:ListNode
        '''
        def reverseList(head, k):
            pre = None
            cur - head
            while cur and k > 0:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
                k -= 1
            head.next = cur
            return cur, pre

        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        if length < k:
            return head

        step = length / k
        ret = None
        pre = None
        p = head
        while p and step:
            next, newHead = reverseList(p, k)

            if ret is None:
                ret = newHead
            if pre:
                pre.next = newHead
            pre = p
            p = next
            step -= 1

        return ret
