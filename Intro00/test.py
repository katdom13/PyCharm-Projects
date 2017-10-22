import random
import numpy as np

randArray = [1,2,3,4,5,6]

access = [0,3]

for x in access:
    print(randArray[x],end=" ")

#=================

print(np.random.randint(0,6))

#=================

env_list = ['*', 'T', '-', 'o']

print(env_list.index('T')-env_list.index('o'))
print(np.abs(-2))

list = ['-']*6
list.insert(1, 'T')

print(list)
print(env_list)

GOAL = 0

def change():
    GOAL = 5

GOAL = 3

change()



print(GOAL)