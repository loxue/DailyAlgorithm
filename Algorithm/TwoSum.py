# -*- coding:utf-8 -*-
'''
    题目：两数之和问题
    给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

    你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

    示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9

    所以返回 [0, 1]

    注：数组、哈希表

    思路：
    1—）暴力法
    2-）一遍哈希表
    3-）两遍哈希表

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d :
                return [d[target - num], i]
            d[num] = i
