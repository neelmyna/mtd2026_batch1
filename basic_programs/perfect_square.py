# Check if a number is Perfect Square

'''
36     6.0     6     36
55     7.4     7     49
150    12.2    12   144

Read a positive interger number as input number, say N

find ROOT of N
convert the ROOT into int // ROOT = floor(ROOT)
check if ROOT ** 2 is equal to N

YES:
    print: N is a Perfect Square
ELSE:
    print: N is not a Perfect Square
'''

# print('Enter a number to check if it is POerfect Square')
# input_number = input()

import math

input_number = int(input('Enter a number to check if it is Perfect Square: '))

if input_number > 0:
    root = math.sqrt(input_number)
    root = math.floor(root) # remove precision part from the number
    if root * root == input_number: # root ** 2
        print(f'{input_number} is a Perfect Square')
    else:
        print(input_number, ' is not a Perfect Square')
else:
    print('We may not be able to find a negative number to be a Perfect Square or not')