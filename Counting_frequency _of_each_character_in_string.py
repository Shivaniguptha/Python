#  Take an input of a String and print in order the frequency of each character occurring in that string. 

s = 'Install the latest PowerShell for new features'
s = s.lower()

# making a copy of s 
a = s
a=set(a)
a.remove(' ')
sum=0

for i in a:
    x=s.count(i)
    print(i, s.count(i))
    sum=sum+x

print(sum)
