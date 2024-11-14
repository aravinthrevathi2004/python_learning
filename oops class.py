# class goa:
#     name=""
#     age=0
#     vehicle=""

#     def beach(self):
#         print("beach............")

#     def hotel(self):
#         print("food.................")
        
# objgoa=goa()

# objgoa.name="aravinth"
# objgoa.age=20
# objgoa.vehicle="train"

# objgoa2=goa()

# objgoa2.name="praveen"
# objgoa2.age=21
# objgoa2.vehicle="bike"

# print(objgoa.name)
# # objgoa.beach()
# print(objgoa2.name)
# objgoa.beach()


# constructor:

# class goa:
#     def __init__ (self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place

#     def getfunc(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("place:",self.place)

#     def setall(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place


# objgoa=goa("aravinth",20,"train")
# objgoa.getfunc()

# objgoa.age=21
# objgoa.getfunc()

# objgoa1=goa("praveen",22,"bike")
# objgoa1.getfunc()

# objgoa1.place="pondy"
# objgoa1.getfunc()

# objgoa1.getfunc()
# objgoa1.setall("kavi",22,"pondy")
# objgoa1.getfunc()


# task:

# 1   create class student:

# class student:
#     def __init__(self,name,mark,subject):
#         self.name=name
#         self.mark=mark
#         self.subject=subject

#     def getall(self):
#         print("name:",self.name)
#         print("mark:",self.mark)
#         print("subject:",self.subject)

# objstu=student("aravinth",500,"tamil")
# objstu.getall()

# # objstu.mark=600
# # objstu.getall()


# objstu2=student("praveen",500,"english")
# objstu2.getall()

# objstu3=student("kavi",300,"maths")
# objstu3.getall()


# objstu4=student("hari",350,"science")
# objstu4.getall()




# 2---create a class caled laptop. create a following variables and function.
        # var=price,proccecsor, ram
        # create object as lenove,hp,dell


# class laptop:
#     def __init__(self,price,proccessor,ram):
#         self.price=price
#         self.proccessor=proccessor
#         self.ram=ram

#     def getfunc(self):
#         print("price:",self.price)
#         print("proccessor:",self.proccessor)
#         print("ram:",self.ram)

# lenove=laptop(50000,"i5","8gp")
# lenove.getfunc()

# hp=laptop(55000,"i7","12gp")
# hp.getfunc()

# dell=laptop("45000","i5","8gp")
# dell.getfunc()



# 3---create class called kodaikanal and create all the possible variables and functions

# class kodaikanal:
#     def __init__(self,budget,place,vehicle):
#         self.budget=budget
#         self.place=place
#         self.vehicle=vehicle

#     def getfunc(self):
#         print("budget:",self.budget)
#         print("place:",self.place)
#         print("vehicle:",self.vehicle)

# kodai=kodaikanal("50000","waterfalls","bike")
# kodai.getfunc()

# kodai2=kodaikanal("2000","hotel","cycle")
# kodai.getfunc()