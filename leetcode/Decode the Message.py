class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dup_key = set(key)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ref_key=""
        res=""
        if ' ' in dup_key:
            dup_key.remove(' ')

        for i in range(0,len(key)):
            if key[i] in dup_key:
                ref_key=ref_key + key[i]
                dup_key.remove(key[i])          

        for i in range(0,len(message)):
            if (message[i]==' '):
                res=res+" "
            else:    
                index = ref_key.index(message[i])
                res=res+alphabet[index]
        
        return res
