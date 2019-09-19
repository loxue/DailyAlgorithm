# -*- coding:utf-8 -*-
'''
    题目：无重复字符的最长字串
    给定一个字符串，找出不含有重复字符的最长子串的长度。
   （注意：是字串不是子序列，二者有很大的区别）

    示例：
    给定 "abcabcbb" ，没有重复字符的最长子串是 "abc"，那么长度就是3。
    给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
    给定 "pwwkew" ，最长子串是 "wke"，长度是3。请注意答案必须是一个子串 ，"pwke"是子序列而不是子串。


    注：此题考查的知识点：双指针、字符串、哈希表
    思路：
    1-）暴力法
    2-）滑动窗口
    3-）优化的滑动窗口（HashMap）

'''


class Solution(object):
    def _lengthOfLongestSubstring(self, s):
        """
        :type s:str
        :rtype: int
        """
        d = collections.defaultdict(int)
        l = ans = 0
        for i, c in enumerate(s):
            while l > 0 and d[c] > 0:
                d[s[i-l]] -= 1
                l -= 1
            d[c] += 1
            l += 1
            ans = max(ans, l)
        return ans

    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i- start + 1)
        return searchInsert
