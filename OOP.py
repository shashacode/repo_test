#creating the simplest possible class that exists
# class Person:
    # pass

##create an object from the person 
# ade = Person()

# Person()
# print(type(ade))

#person class with class instance_specific attributes
# class Person:
#     #attributes
#     name = 'ade'
#     age = 20
#     build = 'muscular'

#instantiating
# class Person:

#     num_of_eyes = 2 #class attribute

#     def __init__(self,name,age,build): #instance attributes

#         self.name = name
#         self.age = age
#         self.build = build


# ade = Person('ade', 23, 'muscular')
# print(ade.name)
# print(ade.age)
# print(ade.build)
# ade.num_of_eyes = 10
# print(ade.num_of_eyes)

# person2 = Person('john', 30, 'skinny')
# print(person2.name)
# print(person2.age)
# print(person2.build)
# print(person2.num_of_eyes)

# import random 
# people = []

# for i in range(10):

#     age = random.randint(15, 60)
#     build = random.choice(['skinny', 'muscular'])
#     name = f'ade{i}'
    
#     people.append(Person(name, age, build))

# for person in people:
#     print(person.name, person.age, person.build, person.num_of_eyes)

#class with methods

# class Person:

#     num_of_eyes = 2 #class attribute

#     def __init__(self,name,age,build): #instance attributes

#         self.name = name
#         self.age = age
#         self.build = build

#     def tell_me_a_story(self):
#         print('that is how the tortise and the hare faded away just like that')

# salau = Person(name = 'salau', age =23, build = 'muscular')
# salau.tell_me_a_story()

#inheritance
# class Warrior(Person):
#     pass

# ogbomevu = Warrior('ogbomevu', '45', 'muscular')
# print(ogbomevu.name)

#polymorphism changing default behaviour of tell me a story mrthod
# class Warrior(Person):
    
#     def tell_me_a_story(self):
#         print(f"{self.name} clears throat. Back 7 full moons and 1 market day ago,the great {self.name} charged into the neighbouring clan and took over.")

# ogbomevu = Warrior('ogbomevu', '45', 'muscular')
# print(ogbomevu.name)
# (ogbomevu.tell_me_a_story())

##instance method
class Person: 

    def __init__(self,name,age,build): #instance attributes

        self.name = name
        self.age = age
        self.build = build

    def tell_me_a_story(self):
        print('that is how the tortise and the hare faded away just like that')


class Warrior(Person):
    def __init__(self,name,age,build, sword, protection): #scope of attribute
        Person.__init__(self, name, age, build)

        self.name = name
        self.sword = sword
        self.protection = protection
    

    def tell_me_a_story(self):
        print(f"{self.name} clears throat. Back 7 full moons and 1 market day ago,the great {self.name} charged into the neighbouring clan and took over.")

# ogbomevu = Warrior('ogbomevu', '45', 'muscular', 'katana', 'odeshi')
# print(ogbomevu.name)
# (ogbomevu.tell_me_a_story())


class Knight(Warrior):
    def __init__(self, name, age, build, sword, protection, num_of_battles, villages): 
        Warrior.__init__(self, name, age, build, sword, protection)

        self.num_of_battles = num_of_battles
        self.villages = villages
        # del self.protection
        # delattr(Warrior, 'protection')

    def tell_me_a_story(self):
        print(f"{self.name} clears throat. Back 7 full moons and 1 market day ago,the great and {self.build} {self.name} charged into the neighbouring clan and took over {self.villages} villages with he's renowned {self.sword} blade.")


import random

names = ['simba', 'kong', 'samurai', 'mufasa', 'panda']
ages = [15, 30, 25, 20, 23]
build = ['muscular', 'skinny', 'skinny', 'plump', 'fat']
protection = ['odeshi', 'metal vest','shield', 'shield', 'metal vest']
sword = ['katana', 'valyrian', 'excalibur' ]

for name, age, build, protection in zip(names, ages, build, protection):
    sword = random.choice(sword)
    protection = random.choice(protection)
    battle = random.randint(3, 100)
    villages = random.randint(3, 100)

    new_Knight = Knight(name, age, build, protection, sword, battle, villages)
    new_Knight.tell_me_a_story()
    print()