# def decor(fun):
#     def decor1():
#         print("please come to my home")
#         fun()
#         print("how is your travel")
#     return decor1
        

# @decor
# def greeting():
#     print("wellcom to my home")

    
# # greeting=decor(greeting)
# greeting()


# task:

review=int(input("enter the review:"))

def decor(fun):
    def decor1():
        print("wellcome praveen")
        fun()
        if review<=5 and review>0:
         print("your review",review)
        print("congratulation praveen, all the best for your future endovers from company")
    return decor1




@decor
def person():
    print("thanks for entering the company")


# person=decor(person)
person()


