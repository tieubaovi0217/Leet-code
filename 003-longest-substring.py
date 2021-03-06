class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        map = {}
        for j in range(len(s)):
            if s[j] in map.keys():
                i = max(i, map[s[j]])
            ans = max(ans, j - i + 1)
            map[s[j]] = j + 1
        return ans

