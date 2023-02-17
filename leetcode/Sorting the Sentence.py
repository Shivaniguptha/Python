class Solution:
    def sortSentence(self, s: str) -> str:
        l=[]
        s=list(s.split(" "))
        n=1

        for j in range(0,len(s)):
            for i in range(0,len(s)):
                if n==int(s[i][-1]):
                    l.append(s[i][:-1])
                    n=n+1
                    
        return " ".join(l)
