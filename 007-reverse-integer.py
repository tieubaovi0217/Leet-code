class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1:
            return 0
        sign = False
        if x < 0:
            sign = True
            x  =  x * (-1)
        x = int(str(x)[::-1])
        if sign == True:
            return x * -1
        return x