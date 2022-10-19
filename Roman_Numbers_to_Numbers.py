def roman(j,x):
        if j=='i':
            x=1
        elif j=='v':
            x=5
        elif j=='x':
            x=10
        elif j=='l':
            x=50
        elif j=='c':
            x=100
        elif j=='d':
            x=500
        elif j=='m':
            x=1000
        return x

n=input('Enter a roman number:')
sum=0
flag=0
x=0
n=n.lower()

for i in range(0,len(n)-1):
    a=int(roman(n[i],x))
    b=int(roman(n[i+1],x))
    if flag==1:
        flag=0
        continue
    if a<b:
        #print(sum,'=',sum,'+',roman(n[i+1]),"-",roman(n[i]))
        sum=sum+roman(n[i+1],x)-roman(n[i],x)
        flag=1
    else:
        #print(sum,'=',sum,'+',roman(n[i]))
        sum=sum+roman(n[i],x)
        
print(sum)
