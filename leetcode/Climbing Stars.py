class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        if n==1:
            return n1
        elif n==2:
            return n2
        else:
            for i in range(0,n-2):
                temp = n2
                n2 = n1 + n2
                n1 = temp
            return n2
