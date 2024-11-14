import collections

# counters


# mylist=["orange","apple","banana","graphs","apple","orange","banana"]
# res=collections.Counter(mylist)
# print(res)


# orderd dict

# mydict=collections.OrderedDict()

# mydict["w"]=1
# mydict["f"]=2
# mydict["k"]=3
# mydict["h"]=5

# # for i,j in mydict.items():
# #     print(i,j)

# mydict.pop("w")
# # for i,j in mydict.items():
# #     print(i,j)

# mydict["w"]=1
# for i, j in mydict.items():
#     print(i,j)


# default dict


# d=collections.defaultdict(int)
# mylist=[4,65,2,2,75]
# for i in mylist:
#   d[i]+=1
# print(d)



# mydict=collections.defaultdict(int)
# mylist=[3,5,6,7,3,4,5,3,67,8,3]
# for i in mylist:
#     mydict[i]+=1
# print(mydict)


# chainmap:

# mylist1=[45,667,43,2]
# mylist2=[45,34,2,32,6]
# mylist3=[23,54,6,786,32]
# res=collections.ChainMap(mylist1,mylist2,mylist3)
# print(res)


# namedtuple:

# student=collections.namedtuple("student",["name","age","place"])
# res=student("aravinth","20","pondy")
# print(res)

# deque:

# name=collections.deque([2,4,5,6])
# name.append(0)
# print(name)

# name.appendleft(7)
# print(name)