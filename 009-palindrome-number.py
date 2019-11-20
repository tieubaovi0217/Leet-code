class Solution:
    def isPalindrome(self, x: int) -> bool:
        first = str(x)
        second = str(x)
        # reverse the string second
        second = second[::-1]
        return first == second