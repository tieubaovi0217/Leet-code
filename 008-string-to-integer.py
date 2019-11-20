class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == '':
            return 0
        pattern = re.compile('^[+-]?\d+')
        x = pattern.findall(str)
        num = 0
        if x != []:
            try:
                num = int(x[0])
                if num > 2**31-1:
                    return 2**31-1
                elif num < -2**31:
                    return -2**31
            except ValueError as err:
                pass
        else:
            pass
        return num