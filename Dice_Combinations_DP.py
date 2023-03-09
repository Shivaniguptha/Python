n = 4
l2 = [1]

for i in range(2,n+1):
    sum = 1
    for j in range(1,i):
        sum = sum + l2[j-1]
    l2.append(sum)
    
print(l2[n-1])
    
#OUTPUT: 8
