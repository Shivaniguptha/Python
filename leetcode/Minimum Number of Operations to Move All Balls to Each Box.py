boxes = "001011"
start = 0
total_boxes = len(boxes)
l=[]

for i in range(0, total_boxes):
    count=0
    for j in range(0, total_boxes):
        if (j == start):
            continue
        
        if (int(boxes[j])==1):
            count = count + abs(start-j)
    
    start = start + 1   
    l.append(count)
    
print(l)
    
#OUTPUT: [11, 8, 5, 4, 3, 4]
