# x = 20

# def do_somthing():

#     x = 30
#     print(x)
#     return 23

# do_somthing()
# print(x)
 
# def greet(name, gender,age):

#     if gender == "male":
#         print(f"Hello Mr {name} {age}...!" if age > 18 else f"Hello Master {name} {age}...!" )
#     # if age < 18:
#     #     print(f"Hello master {name} {age}...!")

#     elif gender == "female":
#         print(f"Hello Mrs {name} {age}....!" if age > 18 else f"Hello Miss {name} {age}...!")


#     # else:

#     #     print(f"Hello Mrs {name} {age}...!")

# # greet("Ade", "male", 13)

# people = [("shade", "female", 60), ("ade", "female", 15), ("sholu", "female", 30), ("manny", "male", 50), ("tolu", "male", 13)]

# for i in people:
#     greet(i[0], i[1], i[2])
#    # or
# # for name, gender in people:
# #        greet(name, gender)
#     #ass hangman greet(name, gender, age, miss or mr)

    

# def f():
#     s = '..inside f()'
#     print(s)

# print('before calling f()')
# f()
# print('after calling f()')

# def f(price = 1.24):
#     print(f"${price}")

# f(price = 3)
# print(f)


# x = {2, 3, 4}
# y = {5, 6, 7}
# if x < y :
#     print('true')

# def say_hello(name):
#     """ THIS IS A DOCSTRING I'M A DESCRIPTOR """

#     print(f"Hello {name}.")
# say_hello('flora')

# def sqrt(number, power):

#     answer = number**(1/power)
#     # print(answer)
#     return answer
# # x = sqrt(9,2)

# # y =(sqrt(9,2) * sqrt(4,2))
# # print(y)

# def root (number, power):
#     answer = number**power
#     return answer

# a = root(4, 2)
# b = root(3, 2)

# def add(a, b):
#     answer = a + b
#     # print(answer)
#     return answer
# p = add(a, b)

# z = sqrt(p  , 2)

# print(z)

# #or
# value = sqrt((a**2) + (b**2), 2)
# print(value)

# import datetime

# # time_now = datetime.datetime.now()
# # print(time_now.weekday()) #gives week day in numerals
# # print(time_now.strftime("%a %H:%M")) #gives a formatted string rep of the time

# # time_stamp = time_now.strftime("%a %H:%M.")

# def get_timestamp():
#     time_now = datetime.datetime.now()
#     time_stamp = time_now.strftime("%a, %b %d %H %M")

#     return time_stamp
 
# def store_memory(memory, time_stamp,txt_len):

#     file = open(f"{time_stamp}-{txt_len}.txt" , "w") 
#     file.write(memory)
#     file.close()

#     return True

# def get_text_len(text):
#     return len(text)

# text = input("please enter a text: ")
# time_stamp = get_timestamp()

# store_memory(text, time_stamp, get_text_len(text))

# def print_nums(one = 1, two = 4, three = 6):

#     print("one: ",one, "two:", two,"three:" ,three) #for keyword argument
# # print_nums(2,1,3) #positional argument
# print_nums() #default arg

 #function with variable positional argument comes in a tuple
# def sum_nums(*args):
#      print(args)

# sum_nums(1,1,2,4,7,5,9)

#function with variable keyword argument comes in a dictionary
def sum_nums(**kwargs):
    print(kwargs)

sum_nums(x = 2, y = 3, z = 4, q = 6)

#zips

# word = list("alphabet")
# numbers = list("12345678")

# zipped_vals = zip(word, numbers)
# print(next(zipped_vals))
# print(list(zipped_vals))

#map
# def mini(x):
#     return "A" + str(x)

    #lambda
# mini2 = lambda x: "A" + str(x)

# # mapped_result = map(mini, numbers)
# # print(list(mapped_result))

# mapped_result2 = map(mini2, numbers)
# print(list(mapped_result2))

#PIP INSTALL REQUESTS
