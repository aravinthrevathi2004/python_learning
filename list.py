# mylist=["apple","orange","tree",1,2,5,7,"true","false"]
# print(type(mylist))

# name=list(("apple","orange","tree",1,2,5,7,"true"))
# print(type(name))
# print(len(name))
# print(name[2])

# mylist=["apple","orange","tree",1,2,5,7,"true","false"]

# print(mylist[1:5])
# print(mylist[4:])
# print(mylist[:4])
# print(mylist[-7:-4])
# print("aravinth" in mylist)   


# mylist[4]="bee"
# print(mylist)


# task

# 1-in a list of array store even or odd numbers in new list and print

# mylist=[1,2,3,4,5,6,7,8,9]
# even_number=[]
# odd_number=[]
# for i in mylist:
#     if i%2==0:
#         even_number.append(i)
#     elif i%2!=0:
#         odd_number.append(i)
# print(odd_number,"odd number")
# print(even_number,"even number")

# 2-print sum of list

# mylist=[1,2,3,4,5]
# sum=0
# for i in mylist:
#          sum=sum+i
#          print(sum)
        
# 3-product of list when zero in list it cant product that number

# mylist=[1,2,3,0,4,5,8]
# product=1
# for i in mylist:
#     if i==0:
#         continue
#     else:
#         product*=i
# print(product)

# 4-find duplicate element in a array and print in new array

# name=["apple","orange","graphs","apple","banana"]
# new=[]
# for i in name:
#     if name.count(i)>1:
#         new.append(i)
# print(new)


# 5-largest and smallest number in a list

# mylist=[2,3,6,4,8,4,3]
# max=mylist[0]
# i=0
# while i<len(mylist):
#    if mylist[i]>max:
#     max=mylist[i]
#    i=i+1
# print(max)
# largest=max(mylist)
# smallest=min(mylist)
# print("largst number=",largest)
# print("smallest number=",smallest)





# 6-reverse a list

# mylist=[2,3,6,4,8,4,3]
# mylist.reverse()
# print(mylist)


