# tuple:
# >> tuple are store multiple items in single variable.
# >> it is orderd ,unchangable and allow duplicate.
# >> tuple declared by round braket
#
# name = ("apple", "banana",3,5,7,True)
# print(len(name))
# print(name[4])
# print(type(name))

# mytuple=tuple(("apple", "banana",3,5,7,True))
# print(type(mytuple))

# print(name[2])------------------------positive index
# print(name[2:])
# print(name[:2])
# print(name[2:5])

# print(name[-2])----------------------negative index
# print(name[-2:])
# print(name[:-2])
# print(name[-5:-2])

# name = ("apple", "banana",3,5,7,True)--------------change into tuple to list(add)
# new=list(name)
# new.append("nee")
# name=tuple(new)
# print(new)

# name = ("apple", "banana",3,5,7,True)---------------(remove)change tuple to list
# x=list(name)
# x.remove("banana")
# name=tuple(x)
# print(x)

# name = ("apple", "banana",3,5,)-----------(unpacking)
# (one,two,three,four)=name
# print(one)
# print(two)
# print(three)
# print(four)


# name = ("apple", "banana",3,5,)----------(asterisk)
# (one,*two,three,four)=name
# print(one)
# print(two)
# print(three)
# print(four)


# nname = ("apple", "banana",3,5,7,True)
# x=list(name)
# x.append("pondicherry")
# name=tuple(x)
# print(x)

# name = ("apple", "banana",3,5,7,True)
# x=list(name)
# x.remove("banana")
# name=tuple(x)
# print(x)

# name = ("apple", "banana",3,5,7,True)
# for i in name:
#     print(i)

# for i in range(len(name)):
#     print(name[i])

# i=0
# while i<len(name):
#     print(name[i])
#     i=i+1

# name = ("apple", "banana",3,5,7,True)
# x=(1,6,8,False)
# result=name+x
# print(result)

# name = ("apple", "banana",3,5,7,True)
# result=name*3
# print(result)
# x=[]
# for i in name:
    # x.append(i)
# print(x



# task:

# 1-add a new element in a tuple without using list constructors. I/P=(1,2,3,4,5) o/P=(1,2,3,4,5,6,7,8,9,10)

# mytuple= (1,2,3,4,5)
# newtuple=(6,7,8,9,10)
# result=mytuple+newtuple
# print(result)

# --------------------------------------

# mytuple= (1,2,3,4,5)
# mylist=[]

# for i in mytuple:
#     mylist.append(i)
# mylist.append(6)
# mylist.append(7)
# mylist.append(8)
# mylist.append(9)
# mylist.append(10)
# mytuple=tuple(mylist)
# print(mylist)
    



# 2-add a new element in a tuple without using list constructor.I/P=("python","c","c++") O/P=("python","c","c++","java","java script","node js")

# mytuple=("python","c","c++")
# newtuple=("java","java script","node js")
# result=mytuple+newtuple
# print(result)

# -----------------------------------------

# mytuple=("python","c","c++")
# mylist=[]
# for i in mytuple:
#     mylist.append(i)
# mylist.append("java")
# mylist.append("java script")
# mylist.append("node js")
# print(mylist)
