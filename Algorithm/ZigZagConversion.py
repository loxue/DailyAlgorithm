# -*- coding:utf-8 -*-
'''
    题目：Z字形变换
    将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
    P A H N
    A P L S I I G
    Y I R

    之后从左往右，逐行读取字符： "PAHNAPLSIIGYIR"
    实现一个将字符串进行指定行数变换的函数:
    string convert(string s, int numRows);

    示例 1:
    输入: s = "PAYPALISHIRING", numRows = 3
    输出: "PAHNAPLSIIGYIR"

    示例 2:
    输入: s = "PAYPALISHIRING", numRows = 4
    输出: "PINALSIGYAHRPI"
    解释:

    P I N
    A L S I G
    Y A H R
    P I

    思路：按行排序、按行访问

'''

class Solution(object):
    def convert(self, s, numRows):
        '''
        :type s: str
        :type numRows: int
        rtype: str
        '''
        if numRows <= 1:
            return s
        n = len(s)
        ans = []
        step = 2 * numRows - 2

        for i in range(numRows):
            one = i
            two = -i
            while one < n or two < n:
                if 0 <= two < n and one != two and i != numRows - 1:
                    ans.append(s[two])
                if one < n:
                    ans.append(s[one])
                one += step
                two += step

        return "".join(ans)
