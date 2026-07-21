import sys

print(sys.argv) # print value of argv
print(sys.argv[0]) # print 1st element of argv
print(type(sys.argv)) # type of argv
print(type(sys.argv[0])) # type of 1st element of argv
print(type(sys.argv[2])) # type of 3rd element of argv
print(len(sys.argv))

try:
    numbers = [int(element) for element in sys.argv]
    print(numbers)
except ValueError as e:
    print('Invalid type of data is given by the user')
    print(e)
finally:
        print('Compulsory statement')
print('Statement after the exception handling')