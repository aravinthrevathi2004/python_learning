# set:
# >> it is unordered, unchangable, and do not allowed dublicate values
# >> it is declared by cursive bracket

# name = {"apple", "banana",3,5,7,True}
# print(type(name))

# newname= list{{"apple", "banana",3,5,7,True}}
# print(type(newname))

# name = {"apple", "banana",3,5,7,True}
# for i in name:
#     print(i)

# name = {"apple", "banana",3,5,7,True} --------------membership
# print(True in name)

# name = {"apple", "banana",3,5,7,True}
# name.add("bee")
# name.update("orange")
# print(name)

# myset={"apple", "banana",3,5,7,True}
# newset={0,4,8,1}
# myset.update(newset)
# print(myset)

# myset={"apple", "banana",3,5,7,True}
# myset.remove("banana")
# myset.discard("bee")
# print(myset)

# ------union--------

# myset={"apple", "banana",3,5,7,True}
# newset={0,4,8,1,5,"banana"}
# myset.union(newset)
# print(myset)

# myset={"apple", "banana",3,5,7,True}
# newset={0,4,8,1,5,"banana"}
# result=myset.union(newset)-----------------union
# print(result)

# result=myset.intersection(newset)--------------intersection
# print(result)

# result=myset.difference(newset)-----------------difference
# print(result)

# result=myset.symmetric_difference(newset)
# print(result)


# x = {"a", "b", "c"}
# y = (1, 2, 3)
# result=x.union(y)
# print(result)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# result=set1.intersection_update(set2)
# print(result)