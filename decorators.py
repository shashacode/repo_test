# def decor(func_to_decorate):

#     def wrapper():

#         print("decorating function")
#         return func_to_decorate( )
#         # print('further decorating function')

#     return wrapper

# @decor
# def func_to_decorate():
#     print('welcome you are logged in!!')

# func_to_decorate()

# secret = 'hello this is a secret'
# def password_required(target):

#     def action():
#         print('sorry this function has been decorated...!!\n')
#         password = input("please enter password: ")
#         set_password = '1233'

#         if password == set_password:
#             print('password correct...!!!\n\n')
#             target()
#         else:
#             print('incorrect password...!!!\n\n')

#     return action

# @password_required
# def show_secret():
#     print(secret)

# show_secret()

# num1 = 2
# num2 = 10


# def must_be_multiple_of_two(number_multiplier):

#     def multiple():
#         print('numbers must be a multiple of 2')

#         if num1%2 == 0:
#             print('proceed')
#             if num2%2 == 0:
#                 print('continue')
#                 number_multiplier()
#         else:
#             print('end')

#     return multiple

# @must_be_multiple_of_two
# def number_multiplier():
#     print(num1 * num2)

# number_multiplier()


#decorating functions that requires arguments and handling their return value


def must_be_multiple_of_two(func_to_decorate):

    def wrapper(num1, num2):
        if num1%2 == 0 and num2%2 == 0:
            func_to_decorate(num1, num2)
        else:
            print('sorry the input numbers is not a multiple of 2')
    return wrapper

@must_be_multiple_of_two
def number_multiplier(num1, num2):
    print(num1 * num2)

number_multiplier(24, 40)
    