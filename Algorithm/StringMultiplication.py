# -*- coding:utf-8 -*-
'''
    题目：字符串相乘问题：
    给定两个以字符串形式表示的非负整数num1和num2，返回num1和num2的乘积（结果仍未字符串形式）

    示例 1:
    输入: num1 = "2", num2 = "3"
    输出: "6"

    示例 2:
    输入: num1 = "123", num2 = "456"
    输出: "56088"

    说明：
    num1 和 num2 的长度小于110。
    num1 和 num2 只包含数字 0-9 。
    num1 和 num2 均不以零开头，除非是数字 0 本身。
    不能使用任何标准库的大数类型（比如BigInteger）或直接将输入转换为整数来处理 。

    思路：竖式乘法

'''

class Solution(object):
    def multiply(self, num1, num2):
        '''
        :type num1:str
        :type num2:str
        :rtype str
        '''
        ans = [0]*(len(num1) + len(num2))
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                ans[i + j] += int(n1) * int(n2)
                ans[i + j + 1] += ans[i + j] / 10
                ans[i + j] %= 10
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()

        return "".join(map(str, ans[::-1]))
