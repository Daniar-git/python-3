# FirstName = str(input("Your first name:"))
# LastName = str(input("Your last name"))
# age = int(input("Your age:"))
# number = input("Your phone number:")
#
# print(f"Your first name is {FirstName} , your second name is {LastName}")
# print("Your age is ",age )
# print("Yo  ur phone number is  ",number )

# Second
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print("Area of торт бурыш is" , a*b)

# Third
# import math
# num = float(input("Enter number"))
# temp = math.floor(num)
# print(temp)
# print(int((num-temp)*100*100) , "," , temp/100)

# Fourth
# import math
# A = int(input("Enter A"))
# print("Y is equal to " , math.pow(A,2)/3 + (math.pow(A,2) +4 )/6 + math.sqrt(math.pow(A,2)+4)/4 + math.sqrt(math.pow(math.pow(A,2)+4,3))/4)

# Fifth

# Second page
# number = int(input("Enter number"))
# print((number*5+8)*2)
# 2.1

# num1 = int(input("First number:"))
# operation = input("Operation:")
# num2 = int(input("Second number:"))
# if operation in ('+','-','*','/'):
#     if operation == "+":
#         print(num1 + num2)
#     elif operation == "-":
#         print(num1-num2)
#     elif operation == "*":
#         print(num1*num2)
#     else:
#         print(num1/num2)
# else:
#     print("It's common calculator")

# 2.2

# num1 = int(input("First number:"))
# operation = input("Operation:")
# num2 = int(input("Second number:"))
# def calc(num1,operation,num2):
#     if operation in ('+','-','*','/'):
#         if operation == "+":
#             return (num1 + num2)
#         elif operation == "-":
#             return (num1-num2)
#         elif operation == "*":
#            return (num1*num2)
#         else:
#             return (num1/num2)
#     else:
#         return ("It's common calculator")
# print("Number 2 is 0") if( num2 == 0 and operation == "/" )else print(calc(num1,operation,num2))

# 2.3

# number = 14
# if(number>10 and number!=12 and number<=15 or number==18):
#     print("True")

# 2.4

# start = 34
# end = 67
# hod = 2
# while (start<end - end%hod):
#     start+=2
#     print(start)

# 2.5
# Srevnenie1 = 10
# Srevnenie2 = 10
# while Srevnenie1!=Srevnenie2:
#     print("Nothing")
# while True:
#     if Srevnenie1==Srevnenie2:
#         print("First interation")
#         break

# 2.6

# for number in range(1,101):
#     if(number!=50 and number!=99):
#         print(number)

# 2.7(Last)
# def printing(letter,number):
#     print(letter * number)
# word = str(input("Enter the word "))
# number = int(input("Enter the number "))
# word = tuple(word)
# for letters in word:
#     printing(letters , number)