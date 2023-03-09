class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lower()
        letters = "abcdefghijklmnopqrstuvwxyz"
        count = 0


        for i in range(0,len(s)):
            if s[i] in letters:
                count = count+1
                final_count = count
            
            if s[i] == "\0":
                    final_count = count
                    
            if s[i] == " ":
                count = 0
            
        return (final_count)
