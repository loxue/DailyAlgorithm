# -*- coding:utf-8 -*-
'''
    题目：反转整数
    给定一个 32 位有符号整数，将整数中的数字进行反转。

    示例 1:
    输入: 123
    输出: 321

    示例 2:
    输入: -123
    输出: -321

    示例 3:
    输入: 120
    输出: 21

    注意:
    假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2 31 ,  2 31 − 1]。
    根据这个假设，如果反转后的整数溢出，则返回 0。

    思路：弹出和推入数字 & 溢出前进行检查

'''

class Solution(object):
    def reverse(self, x):
        '''
        :type x: int
        :rtype : int
        '''
        sign = x < 0 and -1 or 1
        x = abs(x)
        ans = 0

        while x:
            ans = ans * 10 + x % 10
            x /= 10
        return sign * ans if ans <= 0x7fffffff else 0
