class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=="type":
            r_k=0
        elif ruleKey=="color":
            r_k=1
        else:
            r_k=2
            
        for i in range(0,len(items)):
            if items[i][r_k]==ruleValue:
                count=count+1

        return count
