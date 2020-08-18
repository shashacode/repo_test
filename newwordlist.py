


file_name = "wordlist.txt"
file = open(file_name, "r")

data = file.read().split('\n')

import random
words = random.choice(data)

for i in range(30):
    print(random.choice(data))
