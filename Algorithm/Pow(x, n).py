# -*- coding:utf-8 -*-
'''
    题目：Pow(x, n)问题

    实现 pow(x, n) ，即计算 x 的 n 次幂函数。
    示例 1:
    输入: 2.00000, 10
    输出: 1024.00000

    示例 2:
    输入: 2.10000, 3
    输出: 9.26100

    示例 3:
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2(-2次方) = 1/(2*2） = 1/4 = 0.25
'''

class Solution(object):
    def myPow(self, x, n):
        '''
        :type x: float
        :type n: int
        :rtype: float
        '''
        if n < 0:
            n = -n
            x = 1 / x

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >> 1
        return ans
