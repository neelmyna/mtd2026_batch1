import sys

input_number = int(sys.argv[1]) # 10

for i in range(input_number):
    print(f'I = {i}', end=' ')
    i += 2

# 0 3 6 9
# 0 1 2 3 4 
'''
range(number)  [0, number)
range(m, n)    [m, n)
range(m, n, step) [m, n) with increment of step
range(m, n, -step) [m, n) with incremnt of -step
'''