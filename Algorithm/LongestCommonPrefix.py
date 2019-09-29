# -*- coding:utf-8 -*-
'''
    题目：最长公共前缀
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串 "" 。

    示例 1:
    输入: ["flower","flow","flight"]
    输出: "fl"

    示例 2:
    输入: ["dog","racecar","car"]
    输出: ""
    解释: 输入不存在公共前缀。

    说明:
    所有输入只包含小写字母 a-z 。

    思路：分治、二分查找、水平扫描法
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        '''
        :type strs:List[str]
        :stype: str
        '''
        if len(strs) == 0:
            return "" #内容为空值
        i = 0
        j = 0
        end = 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if strs[j][i] != char:
                    break

            if j == len(strs) - 1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1

        return strs[j][:end]
