# print("hello world")

# print(8 * 4) 

# msg = 'Hello world'
# print(msg)

# age = 25
# if age > 20:    
#     print('you are too old')

# print(5/2)

# print(5//2)

# pi_approx = 22/7
# print(pi_approx)
# type(pi_approx)

# print(2 > 3)

# print(2 == 2)
# print(2 == 3)

# x = int (input ('enter an integer: '))
# if x%2 == 0:
#     print('')
#     print('even')

# else:
#         print('')
#         print('odd')

# print('done with conditional')

# name = 'tunde'
# print('name'[2])
# # print(name[:4])

A = ['man', 'woman', 'girl', 'boy'] #list each with its own string
# b = ('Girl, Boy, Woman, Man') #tuple each doesnt need string
# print(A[1])
# print(A[3])
# print(A[-1])
# print(A[0:4]) #gives a particular set of num
# the above tells the position via index
# print(A[1:4]) 
# print(A[-4:4])
# print(A[:3 ])
# print(A[0:4] == A[-4:4])
# print(A[:])
# print(A[:] is A)
# print(b[::-1])
  
# print('man'not in A)

# print(A + ['dog','cat'])
# print(A * 2)
# print(len(A))
# print(min(A))
# print(max(A))

# A = 'man'
# print(A[::-4])

# y = ['a','b', ['c','d', ['e','i'],'f','g'],'h','i', ['j','k'], 'j']
# print(y[2][2])
# print(y[2][2][1])
# print(y[2][2][-2])
# print(y[5][1], y[5][0])

#m:n indicates slicing
# print(y[1:4])
# y[2:2] = ['boy', 'girl', 'man', 'woman']
# print(y)
# y += ['boy', 'girl', 'man', 'woman']
# print(y)
# print(['boy', 'girl', 'man', 'woman'] + y )

# a = ['y', 'd']
# a.extend([123])
# print(a)

# a.insert(2, 'cat')
# print(a)

# a.remove('y')
# print(a)
 
# a.pop(0)
# print(a)

# reply_1 = input('a')
# reply_2 = input('b')
# reply_3 = input('c')
# print("The man {0} to the {1} but didn't {2} anyone".format(reply_1, reply_2, reply_3))


# def bubbleSort (alist):
#     for passnum in range(len(alist)-1, 0, -1):
#         for i in range (passnum):
#             if alist [i] > alist [i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp

# alist = [54,26,93,17,77,31,44,55,20]     
# bubbleSort(alist)         
# print(alist)

# reply_1 = 'went'
# reply_2 = 'house'
# reply_3 = 'find'
# print("The man {0} to the {1} but didn't {2} anyone".format(reply_1, reply_2, reply_3))


# sentence = input("please enter your sentence \n with dashes denoting blank point : \n")
# replacements = input("please enter your replacement in order \n seperated by commas :\n")

# #split sentence into words
# sentence_words = sentence.split(" ")

# print(sentence_words)

# #get corresponding replacements
# replacement_words = replacements.split(',')
# replacement_index = 0

# #search and replace dashes with replacement words
# for i in range(len(sentence_words)):

# #find dashes in words of given sentence
#     if sentence_words[i].find("_") != -1:

# #replace dashes with corresponding replacement words
#         sentence_words[i] = sentence_words [i].replace("_", replacement_words [replacement_index])
#         replacement_index+=1

# full_sentence = " ".join(sentence_words)
# print(sentence_words)

prices = [200, 300, 400, 213, 32]
marked = 1.5

for i in range(len(prices)):
     
    prices[i] = prices[i] * marked

print(prices)