import sys

def my_range(*args):
    if len(args) == 0:
        raise TypeError
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3:
        i = args[0]
        if args[2] > 0:
            while i < args[1]:
                yield i
                i += args[2]
        else:
            while i > args[1]:
                yield i
                i += args[2]

# Main code
try:
    input_number1 = int(sys.argv[1])
    input_number2 = int(sys.argv[2])
    step = int(sys.argv[3])


    print('Range with one argument:')
    for i in my_range(input_number1):
        print(i, end = '\t')

    #if len(sys.argv) == 4 and int(sys.argv[3] > 0):
    print('\n Range with two arguments:')
    for i in my_range(input_number1, input_number2):
        print(i, end = '\t')
    
    print('\n Range with three arguments')
    for i in my_range(input_number1, input_number2, step):
        print(i, end = '\t')
    
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
