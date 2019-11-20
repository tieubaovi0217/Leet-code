class Solution:
    def extendPalindrome(self, s: str, left: int, right: int) -> int:
        ans = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            ans = right - left + 1
            left -= 1
            right += 1
        return ans

    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) < 1:
            return ""
        ans = -1
        start, end = 0, 0
        for i in range(len(s) - 1):
            if (len(s) - i) * 2 < ans:
                continue
            l1 = self.extendPalindrome(s, i, i)
            l2 = self.extendPalindrome(s, i, i + 1)
            if l1 > l2 and l1 > ans:
                ans = l1
                start = i - (l1 - 1) // 2
                end = i + (l1 - 1) // 2
            elif l2 > l1 and l2 > ans:
                ans = l2
                start = i - (l2 - 2) // 2
                end = i + 1 + (l2 - 2) // 2
        return s[start:end + 1]