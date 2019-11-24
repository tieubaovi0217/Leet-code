class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        ans = ''
        for j in range(len(strs[0])):
            ch = strs[0][j]
            ok = True
            for i in range(1, len(strs)):
                if j < len(strs[i]) and ch != strs[i][j] \
                    or (j >= len(strs[i])):
                    ok = False
                    break
            if ok:
                ans += ch
            else:
                break
        return ans