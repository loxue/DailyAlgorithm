# -*- coding:utf-8 -*-
'''
    题目：下一个排列问题

    实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
    如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
    必须 原地 修改，只允许使用额外常数空间。

    以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

    思路：暴力法、一遍扫描
'''

class Solution(object):
    def nextPermutation(self, nums):
        '''
        :type nums: List[int]
        rtype: void Do not return anything, modify nums in-place instead.
        '''
        if nums is None or len(nums) <= 1:
            return

        pos = None
        p = len(nums) - 2
        # find the first number that is not in corrent order

        while p >= 0:
            if nums[p + 1] > nums[p]:
                pos = p
                break
            p -= 1

        if pos is None:
            self.reverse(nums, 0, len(nums) - 1)
            return
        # find the min value in the rest of the array
        minPos, minV = pos + 1, nums[pos + 1]
        for i in xrange(pos + 1, len(nums)):
            if nums[i] <= minV and nums[i] > nums[pos]:
                minV = nums[i]
                minPos = i
        # swap the two above number and reverse the array from 'pos'
        nums[pos], nums[minPos] = nums[minPos], nums[pos]
        self.reverse(nums, pos + 1, len(nums) - 1)


    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
