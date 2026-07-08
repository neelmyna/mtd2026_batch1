# Accept the average score from the user and print the result. Also check if the input is wrong.
'''
Accept the average score from user (The percentage may be a floating point number)
Print the result as follows:
    0 to 49 Fail
   50 to 69 Second Class
   70 to 89 First Class
   90 to 100 Distiction
'''

average_score = float(input('Enter average score of the student: '))
if average_score < 0 or average_score > 100:
    print('Invalid Iput entered')
elif average_score <= 49:
    print('Result is Fail')
elif average_score <= 69:
    print('Result is Second Class')
elif average_score <= 89:
    print('Result is First Class')
else:
    print('Result is Distinction')