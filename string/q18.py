"""
问题描述：给定一个字符串str，返回str的最长无重复字符子串的长度。

举例：
str="abcd"，返回4
str="aabcb"，最长无重复字符子串为"abc"，返回3

要求：
如果str的长度为N,请实现时间复杂度为O(N)的方法。
"""


class LongestNotRepeatStr:
    @classmethod
    def get_longest_sut_str(cls, strs):
        d = set()
        for i in strs:
            if i not in d:
                pass