import sys

input_number = int(sys.argv[1])
print(type(sys.argv))
print(type(sys.argv[0]))
print(sys.argv[0])

print(f'The user given number is {input_number}')

# 12 * 1 = 12
# 12 * 2 = 24
for i in range(1, 21):
    #print(f'{input_number} * {i} = {input_number * i}')
    # print(input_number, ' * ',i, ' = ', input_numner * i )
    print('%2d * %02d = %03d'%(input_number, i, input_number * i))
