# #fibbonaci
# quantity = 5

# x = 0
# y = 1
# print(x)
# print(y)

# for i in range(quantity):
#     print(x + y)
#     x, y = y, x+y

# x = 0
# y < 50
# print(x)
# print(y)

# for i in range(0,50):
#     print(x + y)
#     x, y = y, x+y

# a = [1,0,0,2]
# print(a[::-1])

# q = [1,2,3,4,5,6,7,8,9,10]
# print(q[4:8])
# print(q[-1]) 

students_score= [
    [   "atha",
        [
                ["m", 30],
                ["e", 30]
        ],
        [
            "hobby",[
                ["singing", 20],
                ["dancing", 10]
            ]
        ]
    ],
    ["bolu", [
        ["m" ,30],
        ["e", 30]], [
           [["singing", 20], ["dancing", 10]]
    ]],
    ["seun", [
        ["m" , 30],
        ["e" , 10]],
        [["singing", 20], ["dancing", 10]]
    ]
]
    

# atha_name = students_score[2][0]
# print(atha_name) 
atha_name = students_score[0][2][1]
print(atha_name)

target_student = students_score[0]

name = target_student[0]
print("name : ", name)

hobbies = target_student[2]

# hobby1 = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1])

# dict

# the_club = {'football:chelsea','basketball:wolves'}
# print(the_club)
# the_club = dict([
#     ('football', 'chelsea'),
#     ('basket', 'loops')
#     ])
# print(the_club)
# the_club = dict(
#     football = 'chelsea')
# print(the_club)
# print(the_club['basket'])
# the_club['town'] = 'texas'
# print(the_club)
# del the_club['town']
# print(the_club)
# print('loops' not in the_club)
# print(len(the_club))

# d  = {'a': 10, 'b': 20, 'c': 30}
# # print(d)
# # print(d.clear())
# print(d.get('a'))
# print(d['a'])

# #set
# # x = set(['man', 'boy', 'girl', 'boy', 'woman'])
# # print(x )
# # y = {'man', 'woman', 'girl', 'girl', 'foo'}
# # print(y)
# # t = 'man'
# # print(set(t))
# # d = set('foo') #gives {'f','o}
# # d = {'foo'} #gives {'foo}
# # print(d)
# # print(y|d)
# # print(y.union(d))
# # print(y.intersection(d))
# # print(y & d)