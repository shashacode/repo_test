# for i in range(1500,2701):
#     if i%5==0:
#         if i%7==0:
#             print(1)

# number = def input('enter a number:')
# int(number[-1])

# print('enter a temperature with F for farenheit and C for celcius')
# temp = input()
# deg = int(temp[:-1])
# unit = temp[-1]
# if unit =="C":
#     if deg > 0 and deg < 100:
#         g = 9*(deg - (5/32))
#         print(f"the value of {deg} farenheit is {g} ")
#     else:
#         print('the degrees are not valid')
# elif unit == "F":
#     if deg > 32 and deg < 212:
#         g = 5*(deg - (32/9))
#         print(f"the value of {deg} celsius is {g}")
#     else:
#         print("the degrees are not valid")
# else:
#     print("enter a valid temperature with correct unit")

# name = 'flora'
# print(name[::-1])

# even_num = 0
# for i in range(1,10):
#     if i%2 == 0:        
#         even_num = even_num + 2
#         print(even_num)


# tempee == 'c':

#   celc_temp_input = float(input('Please enter the temperature : '))

#   fahr_temp_output = (celc_temp_input * (9/5)) + 32

#   print('Your fahrenheit temperature is', fahr_temp_output)

# elif temperature == 'f':

#   fahr_temp_input = float(input('Please enter the temperature : '))

#   celc_temp_output = (fahr_temp_input - 32) * (5/9)

#   print('Your celcius temperature is', celc_temp_output)


# names = ['john', 'paul', 'sean']

# index = 0

# while True:
#     #print(index, names[index])
    
#     names[index] = 'Mr ' + names[index]
    
#     index +=1

#     if index == len(names):
#         break

# print(names)

# names = ['john', 'paul', 'sean']

# for index in range(len(names)):

#     names[index] = 'Mr' + names[index]
# print(names)

# list_of_values_entered= []
# while True:

#     value = input("please enter a value \n: ")
#     list_of_values_entered.append(value)

 #     for value in list_of_values_entered:
#         print(value.center(10), str(len(value)).center(10))

list_of_values_entered = []
 
while True:

    value = input("please enter a value:")

    list_of_values_entered.append(value)
    print("you now have", len(list_of_values_entered), "values in your list")

    stop_or_continue = input("press y to continue entering values or n to stop : ")

    if stop_or_continue == "n":
        break

total_characters = 0 #total num of words

print("value".center(10), "length".center(10), "Qty_A".center(10), "Qty_B".center(10), "Qty_C".center(10) )
for value in list_of_values_entered:

    length_of_value = len(value)
    total_characters += length_of_value
    print(value.center(10), str(length_of_value).center(10), str(value.count("a")).center(10), str(value.count("b")).center(10), str(value.count("c")).center(10))

print(f"\nValues in list : {len(list_of_values_entered)}.  Total characters : {total_characters}.")

# word_list = []
# index = 0 #can hold any number

# for char in "alphabet":
#     index +=1
#     word_list.append((index, char, char.upper()))

# print(word_list)

# x = ['apples', 'berry']
# x +=['tulip', 'mango']
# print(x)

##EXTEND

# nums = [1,2,3,5,6,7]

# nums.insert(3,4)
# print(nums)

# #remove

# nums = [1,2,3,5,6,7,7,7,7,]

# # nums.remove(7)
# # print(nums)
# number_of_sevens = nums.count(7)

# for _ in range (number_of_sevens):
#     nums.remove(7)
     
# print(nums)