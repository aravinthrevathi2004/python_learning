# 1.Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle the exception if the user inputs zero 
# 2.Modify the above program to also handle the exception if the user inputs a non-numeric value
# 3.Write a program that reads a number from the user and prints its square. Use the else clause to print a success message
# 4.Modify the program in Task 3 to include a finally clause that prints a message regardless of whether an exception occurred or not
# 5.Write a function that raises a ValueError if the input number is negative
# 6.Write a program that repeatedly asks the user for a number and handles exceptions. The program should continue asking until a valid number is entered.



# 1.Write a Python program that asks the user to input a number and prints the reciprocal of that number. Handle the exception if the user inputs zero 
# try:
#     num=int(input("enter the number:"))
#     res=5/num
#     print(res)

# except Exception as e:
#     print("exception error",e)


# 2.Modify the above program to also handle the exception if the user inputs a non-numeric value


# try:
#     num=int(input("enter the number:"))
#     res=5/num
#     print(res)

# except Exception as e:
#     print("exception error",e)

# except ValueError:
#     print("value error")

# except NameError:
#     print("name error")


# 3.Write a program that reads a number from the user and prints its square. Use the else clause to print a success message

# try:
#     num=int(input("enter the number:"))
#     res=5/num 
#     result=res**2
#     print(result)

# except Exception as e:
#     print("exception error",e)

# else:
#     print("success")


# 4.Modify the program in Task 3 to include a finally clause that prints a message regardless of whether an exception occurred or not

# try:
#     num=int(input("enter the number:"))
#     res=5/num 
#     result=res**2
#     print(result)

# except Exception as e:
#     print("exception error",e)

# else:
#     print("success")

# finally:
#     print("regardless of whether an exception occurred")

# 5.Write a function that raises a ValueError if the input number is negative

# num=int(input("enter the number:"))
# if num<=0:
#     raise("enter the positive number")


# 6.Write a program that repeatedly asks the user for a number and handles exceptions. The program should continue asking until a valid number is entered.


# num=int(input("enter the number:"))
# if num==str:
#     print("enter the numer")