# inheritance - base class and derived class

# task:

# 1.create a person class and a student class that inherits from person(single)

# class person:
#     def aravinth(self):
#         print("hiii aravinth..........")

# class student(person):
#     def mark(self):
#         print("he got 80 mark in maths.......... ")

# objstu=student()
# objstu.mark()
# objstu.aravinth()


# 2. creatr a class animal ,a mammal class thst inherits from animal,and a dog class that inherits from mammal(multilevel)

# class animal:
#     def cheeta(self):
#         print("cheeta is a fastest animal.........")

# class mammal(animal):
#     def cow(self):
#         print("cow is a mammal.........")

# class dog(mammal):
#     def mani(self):
#         print("the dog name is mani........")

# objmamm=mammal()
# objmamm.cow()
# objmamm.cheeta()

# objdog=dog()
# objdog.mani()
# objdog.cow()
# objdog.cheeta()


# 3.create a class vehicle and two classes car and bike that inherit from vehicle

# class vehicle:
#     def bus(self):
#         print("there is a bus accident.......")

# class car(vehicle):
#     def thar(self):
#         print("thar price is 15,00000 in india......")

# class bike(vehicle):
#     def duke(self):
#         print("duke price is 200000 in india........")


# objcar=car()
# objcar.thar()
# objcar.bus()

# objbike=bike()
# objbike.duke()
# objbike.bus()


# 4.create a teacher class ,a student class that both inherits from person, and an assistant class that inherits from both. 



# class teacher:
#     def professor(self):
#         print("she is a professor in college........")

# class student:
#     def mark(self):
#         print("he got 80 mark in maths.......... ")

# class person(teacher,student):
#     def aravinth(self):
#         print("hiii aravinth..........")


# class assistant(person):
#     def job(self):
#         print("he is assistant in our company.......")

# objper=person()
# objper.aravinth()
# objper.mark()
# objper.professor()

# objass=assistant()
# objass.job()
# objass.aravinth()
# objass.mark()
# objass.professor




# super keywords:



# 1.class a having display function and constructor class b having display function create obi for a. create a obj for b and accecss a 
#   constructor by uding super keywords

# class a:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place

#     def disfun(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("place:",self.place)

# class b(a):
#     def __init__(self, name, age, place):
#         super().__init__(name, age, place)

#     def disfun(self):
#          super().disfun()

# objb=b("aravinth",20,"pondy")
# objb.disfun()


# 2.class c having display function have to inherit class a and clss b constructor.

# class a:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place

#     def disfun(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("place:",self.place)


# class b:
#     def __init__(self,name,mileage,price):
#         self.name=name
#         self.age=mileage
#         self.place=price

#     def disfun(self):
#         print("name:",self.name)
#         print("mileage:",self.mileage)
#         print("price:",self.price)

# class c(a,b):
#     def __init__(self,name,id,mark):
#         self.name=name
#         self.id=id
#         self.mark=mark

#     def disfun(self):
#         print("name:",self.name)
#         print("id:",self.id)
#         print("mark:",self.mark)

# obja=a("aravinth",20,"age")
# objb=b("mt15",45,200000)
# objc=c("praveen",354,500)
# objc=a()

        
