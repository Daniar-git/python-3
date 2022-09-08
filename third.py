# First
# def is_alive(health):
#  if health<0:
#     return "False"
#  else:
#     return "true"
# print(is_alive(5))

# Second
# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December')
#
# def Month(number:int):
#
#     if number<3:
#         return ("White snow fell outside the window , Your birth day is: ",months[number-1] )
#     elif number<6:
#         return ("Birds sang beautiful songs ,Your birth day is: ",months[number-1])
#     elif number<9:
#         return ("The sun shone brighter than ever ,Your birth day is: ",months[number-1])
#     else:
#         return ("The harvest was incredible , Your birth day is: ",months[number-1])
#
# print(Month(9))

# Advanced level

# First(3)
# dict = {
#     "Upper": False,
#     "Lower": False,
#     "Number": False,
#     "Special Characters": False,
# }
# def check_pass(pswd):
#     if(len(pswd) == 8 ):
#         for letter in pswd:
#             if ord(letter)>=65 and ord(letter)<=90:
#                 dict["Upper"] = True
#             elif ord(letter)>=97 and ord(letter)<=122:
#                 dict["Lower"] = True
#             elif ord(letter)>=48 and ord(letter)<=57:
#                 dict["Number"] = True
#             elif ord(letter)>=43 and ord(letter)<=47 or ord(letter)<=64:
#                 dict["Special Characters"] = True
#     else:
#         return "Password must have 8 characters"
#     for keys in dict:
#         if dict[keys] == False:
#             return keys
#         if keys == "Special Characters":
#             return "Everything is great"
# print(check_pass("Ikn0wp@s"))