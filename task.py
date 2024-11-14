mylist=[2,3,6,4,8,4,3]
max=mylist[0]
i=0
while i<len(mylist):
    if mylist[i]>max:
        max=mylist[i]
       
    i=i+1
print(max)
