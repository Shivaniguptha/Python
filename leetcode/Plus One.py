class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        l1=[]

        for i in digits:
            s = s + str(i)
            
        sum = str(int(s) + 1)

        for i in range(0,len(sum)):
            l1.append(int(sum[i]))
            
        return (l1)
