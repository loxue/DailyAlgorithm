# -*- coding:utf-8 -*-
'''
    题目：两数相除问题
    给定两个整数，被除数 dividend 和除数 divisor 。将两数相除，要求不使用乘法、除法和 mod 运算符。
    返回被除数 dividend 除以除数 divisor 得到的商。

    示例 1:
    输入: dividend = 10, divisor = 3
    输出: 3

    示例 2:
    输入: dividend = 7, divisor = -3
    输出: -2

    说明:
    * 被除数和除数均为 32 位有符号整数。
    * 除数不为 0。
    * 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2 31 ,  2 31 − 1]。本题中，
      如果除法结果溢出，则返回 2 31 − 1。

    思路：二分法
'''

class Solution(object):
    def divide(self, dividend, divisor):
        '''
        :type dividend: int
        :type divisor: int
        :rtype: int
        '''
        if divisor == 0:
            return 0x7fffffff
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        ans = 0
        cnt = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        subsum = divisor

        while dividend >= divisor:
            while (subsum << 1) <= dividend:
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            cnt = 1
            dividend -= subsum
            subsum = divisor
        return max(min(sign * ans, 0x7fffffff), -2147483648)
