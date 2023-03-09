s = "hello world"

for i in s:
    val = ord(i)
    
    if (val >= 97) and (val <= 109):
        print(chr(val+13), end="")
        
    elif (val >= 110) and (val <= 122):
        print(chr(val -13), end="")
    
    else:
        print(" ",end="")
        
