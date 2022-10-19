# Given an array Arr of size N, To print second largest element from an array.

n=int(input())
arr=list(map(int,input()))
flag=0
arr.sort()
arr=arr[::-1]
	
for i in arr:
		if arr[0]!=i:
		     flag=1
		     return i
        
if flag==0:
    return -1
