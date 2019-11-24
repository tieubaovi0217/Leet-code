from itertools import product

arr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        for digit in digits:
            ans.append(arr[int(digit)])
        result = list(product(*ans))
        ans = []
        for each_ans in result:
            ans.append(''.join(each_ans))
        return ans

s = Solution()
ans = s.letterCombinations('234')
print(ans)