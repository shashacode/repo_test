import ast

file_name = "data.txt"
file = open(file_name, "r")
data = file.read()

dictionary = ast.literal_eval(data)
# print(dictionary)
print(type(dictionary))

# def unpack (**weather):
#     print(weather)
# unpack()

# def get_time(list):
#     print(zip(dt_txt)) 
# get_time(dt_txt)

# def get_temp(list,main,temp ):
#     weather = file.read
#     for temp in weather:
#         print(temp)