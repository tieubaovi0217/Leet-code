class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '':
            return ''
        ans = [list() for _ in range(numRows)]
        move = []
        while True:
            i = 0
            ok = False
            while i <= numRows - 1:
                move.append(i)
                if len(move) == len(s):
                    ok = True
                    break
                i += 1
            if ok:
                break
            i = numRows - 2
            while i >= 1:
                move.append(i)
                if len(move) == len(s):
                    ok = True
                    break
                i -= 1
            if ok:
                break
        for i in range(len(s)):
            ans[move[i]].append(s[i])
        res = ''
        for r in range(numRows):
            for ch in ans[r]:
                res += ch
        return res