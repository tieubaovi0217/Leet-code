"""
This solution based on the idea of solution section of Leetcode
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '':
            return s == ''
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])