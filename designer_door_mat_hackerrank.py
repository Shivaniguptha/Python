n,m=map(int,input().split())
lines1=int((n-1)/2)
pattern1=0
s1=".|."
s2="---"

while(lines1!=0):
    print(s2*lines1 + s1 + s1*pattern1 + s2*lines1)
    lines1 = lines1 - 1
    pattern1 = pattern1 + 2
    
lines2=int((m-7)/2)
s3="-"
s4="WELCOME"
print(s3*lines2 + s4 + s3*lines2)

lines2=int((n-1)/2)
pattern2 = 1 + (2*(lines2-1))
for i in range(1,lines2+1):
    print(s2*i + s1*pattern2 + s2*i)
    pattern2 = pattern2 - 2
    
    /*
    Sample Designs

    Input: Size: 7 x 21 
    Output: 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    */
