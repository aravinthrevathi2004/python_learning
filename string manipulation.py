# string manipulation

# name='aravinth'
# name="aravinth"
# name=''''aravinth'''
# print(type(name))

# print(name[6])
# print(len(name))

# slicing

# name="we are going to pondicherry"
# print(name[2:12])
# print(name[0:2])
# print(name[1:11])
# print(name[:8])
# print(name[3:])
# print(name[:])

# negative indexing

# print(name[-13:-2])
# print(name[-15:-1])
# print(name[:-8])


# name= "we are going to pondicherry"
# print(name.upper())
# name="WE ARE GOING TO PONDICHERRY"
# print(name.lower())
# print(name.strip())
# print(name.center(60))
# print(name.replace("r","o"))
# print(name.split())

# name="aravinth"
# name2="D"
# result=name+" "+name2
# print(result)

# name="123"
# result=f"pondicherry{name}"
# print(result)

# escape:

# name= "we are going to \"pondicherry\""
# print(name)

# name= "we are going to pondicherry"
# name="WE ARE GOING TO PONDICHERRY"
# print(name.capitalize())
# print(name.casefold())

# print(name.count("we"))
# print(name.endswith("y"))
# print(name.startswith("we"))

# print(name.find("going"))
# print(name.index("g"))


# name= "we are going to pondicherry"

# print(name.encode())
# print(name.find("i"))
# name= "wearegoingtopondicherry"
# print(name.isalnum())
# print(name.isalpha())

# name= "wearegoingtopo%^*(346ndicherry"
# print(name.isascii())

# name="12345"
# print(name.isdecimal())
# print(name.isnumeric())
# print(name.isdigit())

# name="sample"

# print(name.isidentifier())

# name= "we are going to pondicherry"
# print(name.islower())
# print(name.isupper())

# name=("apple","orange","banana")
# print(" ".join(name))

# print(name.split())

# print(name.swapcase())

# task

# 1- In a paragraph replace a "id" with "was" .then count no of "a" in a paragraph.

# para=("success is the sum of efforts, repeated day in and day out")
# result=para.replace("is","was")
# print(result)

# result=para.count("a")
# print(result)

# 2-grt a input from user check its a email id

# email=(input("enter the email id:"))
# if "@"in email and "." in email:
#     print("it is a email id.")
# else:
#     print("enter the correct email id.")

# 3- get a input from user also check its valid password

# num=(input("enter the password:"))
# print(num.isalnum())

# 4-login task-get input from user name & password its align your previous data.throw a login successful message. otherwise its a invalid input

# name="aravinth"
# password="12345"

# name1=input("enter the name:")
# password1=input("enter the password:")
# if name==name1 and password==password1:
#     print("login successful.")
# else:
#     print("invalid input.")

