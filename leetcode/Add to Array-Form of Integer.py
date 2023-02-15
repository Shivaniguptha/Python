class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sum = 0
        l=[]
        numSize=len(num)
        for i in range(0,numSize):
            res=(10**(numSize-1-i));
            sum=sum+(num[i]*res);
            
        sum=sum+k;
        sum=str(sum)
        for i in range(0,len(sum)):
            l.append(int(sum[i]))

        return l
