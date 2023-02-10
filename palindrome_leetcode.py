class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=len(str(x))-1
        i=0
        x=str(x)
        while (l!=0):
            if(x[i]!=x[l]):
                return "false"
            i=i+1
            l=l-1
        return "true"
