import random

# n = random.randint(100000, 999999)
# print(n)
#
# m = random.randbytes(3)
# print(m)
#
# print(random.randrange(1, 10))
#
# mytuple = ("100", "Soumika", "Megha", "Dhoni", "Virat")
# myset = {"100", "Soumika", "Megha", "Dhoni", "Virat"}
# mylist = ["100", "Soumika", "Megha", "Dhoni", "Virat"]
# print(random.choice(mylist))
# print(random.choice(mytuple))
#
# my_list = [1, 2, 44, 2, 425, 34, 97, 856, 599, 905]
# sample_ele = random.sample(my_list, 3)
# print(sample_ele)

import string

s = 10
ran = ''.join(random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, s))
print(str(ran))
s1 = int(input("Enter a number: "))
ran1 = ''.join(random.sample(string.digits, s1))
print(ran1)
