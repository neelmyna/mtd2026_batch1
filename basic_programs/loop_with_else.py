'''
x = 0
y = 2
z = len("Python") # 6
x = y > z # False
print(x) # False
--------------------
i = 250
while i >= 5:
   i //= 2
else:
   i += 2
print(i)

itr=1
    i=125
itr=2
    i=62
itr=3
    i=31    15    7    3

The control goes to else when there is 0 iretarions or even when the loop has few iterations but the loop condition fails at some point of time.

Tell me when the control doesnt go to else???
---------------------------
x = 0
y = 2
z = len("Python") # 6
x = y > z # False
print(x) # False

n = 0
while n < 4:
   n += 1 
   # insert
   print(n, end=' ')

# O/P: 1 2 3 4  (single line O/P)


What will the final value of the Val variable be when the following snippet finishes its execution?

Val = 1
Val2 = 0
Val = Val ^ Val2   # 1
Val2 = Val ^ Val2  # 1
Val = Val ^ Val2   # 0 
print(Val) # 0

x = 25
y = 18
0001 1001

x = 1110 0110
-128 + 64 + 32 + 6
= -64 + 38
x = -26

~ ^ & | << >>

00011001
00010010
00010000
00011011 x | y = 27
x & y = 32
----------------------------
Which line can be used instead of the comment to cause the snippet to produce the following expected output? (Select all that apply)
Code:
z, y, x = 2, 1, 0
x, z = z, y # x = 2, y = 1, z = 1
y = y - z  # x = 2, y = 0, z=1 
x, y, z = y, z, x
# put line here
print(x, y, z) # 0, 1, 2
# Expected output: 0, 1, 2 

# z, y, x = x, z, y

# y, z, x = x, y, z
----------------------------
# What is the expected output of the following snippet?
a = 0
b = a ** 0 # 1
if b < a + 1:
    c = 1
elif b == 1:
    c = 2
else:
    c = 3
print(a + b + c)  # 3
---------------------------
# How many stars (*) does the following snippet print?
i = 10
while i > 0 :
    i -= 3
    print("*")
    if i <= 3:
        break
else:
    print("*")

# How many lines does each of the following code examples output when run separately?
 # Example 1
for i in range(1, 4, 2): # 2
    print("*")
 # Example 2
for i in range(1, 4, 2): # 1
    print("*", end="")  
 # Example 3
for i in range(1, 4, 2): # 1
    print("*", end="**")
 # Example 4
for i in range(1, 4, 2): # 1   
    print("*", end="**")
print("***")


name = 'Akshatha'
name[8]  IndexError
name[2:20]
name[]
name[:]
name[::]
name[::-2]
name[::1]
name[::-1]
'''


