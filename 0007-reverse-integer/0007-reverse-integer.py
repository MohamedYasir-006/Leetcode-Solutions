class Solution:
    def reverse(self, x: int) -> int:
        min=-2**31
        max=2**31-1
        s=str(abs(x))
        rev=s[::-1]
        num=int(rev)
        if x<0:
            num=-num
        if num < min or num > max:
            return 0
        return num
