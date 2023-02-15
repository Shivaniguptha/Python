class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_letter=s[0]
        start_num=s[1]
        temp1=start_num
        end_letter=s[3]
        end_num=s[4]
        length=(ord(end_letter)-ord(start_letter)+1)*(int(end_num)-int(start_num)+1)
        res=[]

        for i in range(0,length):
            a=""
            temp=a+str(start_letter)+str(start_num) 
            start_num=int(start_num)+1
            
            if (int(start_num)==int(end_num)+1):
                start_num=temp1
                start_letter=chr(ord(start_letter)+1)
            res.append(temp)
        return res
