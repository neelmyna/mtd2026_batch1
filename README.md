# MTD 2026 - Batch 1

This repository is created for the **1st Batch of 2026** at **MTD** for the course **Competitive Programming and Java Full Stack**.

---

# Notes

## Organizing Your System

We must organize all files and folders properly in our system.

### Step 1: Create a Software Folder

- Create a folder named **Software** in the **C:** drive.
- Inside the **Software** folder, create one folder for each software you wish to install.
- Download the software setup (`.exe`/`.msi`) file.
- Move (Cut & Paste) the downloaded installer from the **Downloads** folder into its respective folder inside the **Software** folder.
- Install the software by double-clicking the installer from this location.

---

## What Gets Installed?

Whenever we install software, the following components may be installed:

- Program code
- Libraries / Modules / Packages
- Compiler (if applicable)
- Runtime / Execution Environment (if applicable)

To use the software, we generally get one or both of the following types of applications:

1. **CLI (Command Line Interface)**
2. **GUI (Graphical User Interface)**

---

## Examples

### Python

When Python is installed, we get:

- CLI:
  - `python`
  - `pip`
- GUI:
  - **IDLE (Python Shell)**

### Node.js

When Node.js is installed, we get:

- CLI:
  - `node`
  - `npm`

### MySQL

When MySQL is installed, we get:

- CLI:
  - `mysql`
- GUI (Optional):
  - **MySQL Workbench**

---

## Environment Variables (PATH)

Some software installations do not make their CLI commands available globally.

In such cases:

1. Copy the installation path of the executable.
2. Add this path to the **Environment Variables → PATH**.
3. Close and reopen the Command Prompt or Terminal.

> **Note:** The currently opened terminal will not recognize the changes until it is restarted.

---

# Required Software Installations

| Software                         | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| **Notepad++**                    | Quick note taking                             |
| **Visual Studio Code (VS Code)** | IDE / Code Editor                             |
| **Eclipse IDE**                  | Java Development                              |
| **JDK (Java Development Kit)**   | Java Compiler, JVM, and Libraries             |
| **Python**                       | Python Interpreter, Libraries, and IDLE Shell |
| **Git**                          | Run Git commands                              |
| **GitHub Desktop**               | Perform Git operations using GUI              |
| **MySQL**                        | Practice SQL / RDBMS                          |
| **MongoDB**                      | Practice NoSQL (Server & Compass)             |
| **Node.js**                      | Practice JavaScript                           |

---

# Learning Folder

Choose one drive in your laptop (preferably **D:** or **E:** instead of **C:**) for learning purposes.

Create a folder named:

```
Learning
```

If your laptop has only the **C:** drive, create:

```
C:\Learning
```

---

# GitHub Setup

## Step 1: Create a GitHub Account

Create a GitHub account using:

- Your permanent email address
- Your permanent phone number

Login to your account.

---

## Step 2: Create a Repository

Create a new repository with the following name:

```
mtd2026
```

---

## Step 3: Clone the Repository

Clone the repository into your **Learning** folder.

### Steps

1. Open the **Learning** folder.
2. Open the terminal in that folder.
3. Run the following command using your repository URL:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/your-username/mtd2026.git
```

This creates a copy of your GitHub repository inside the **Learning** folder.
The Repo in our laptop will be a folder. And Git can recognise this as a special folder nothing but a Repo folder.

## PUSH and PULL:

push is to upload (from local repo to remote/server/cloud repo)
pull is to download

length() java
strlen() c

Java: byte, short, int, long
mysql: tinyint, smallint, int, bigint

To avoid plagiarism, copy rights, trademarks etc. companies use different names for the same thing.

To update our local repo w.r.t. the remote repo, we must PULL/download.

```bash
git pull
git pull origin main
```

In all repos, at least one branch is always created and its name is **main**
Thus when we run the command:

```bash
git pull
```

We are actually running (by default):

```bash
git pull origin main
```

## Steps to Push:

1. We must 1st tell the git to list the names of the files and folders which are either modified or created or deleted.

```bash
git add <PATH>
git restore --staged .
```

To unlist/unstage the staged files, use the above command.

2. Next step is to commit: Here, the git will create an object and save content of all the files from Step1 into the object and encript the object.

```bash
git commit -m "MESSAGE"
```

3. push

```bash
git push origin <branch name>
git push origin main
git push
```

Note that when ever we create a repo, it will always have one branch namely **main**
This is a default branch.
Hence, both the above 2 commands are one at the same.

## Steps to create Personal Access Token:

1. Click on profile icon (top right corner)
2. Click settings from the list
3. In next page, scroll down and click developer settings (bottom left corner)
4. Next page, on left, click personal access tokens, select tokens classic
5. Next page, click generate new token classic
6. Next page, give a notes
7. Select expiry: No expiry
8. In the list of options, selct the 1st check box Repo
9. Scroll down and click generate token
10. Copy the PAT and mail it to yourself (from one of your gmail to another or same) with mail subject and body as "git pat" and "git_pat" respectively.

---

DAY2 FRIDAY 03-07-2026

## GIT CONFIGURATION COMMANDS

```bash
git config --global user.name "neelmyna"

git config --global user.email "abc@xyz.com"
```

To clone Repo using PAT:

```bash
git clone <Repo_URI>
git clone https://github.com/username/repo_name
git clone https://PAT@github.com/username/repo_name
```

Data is most important. It is the sole reason for programming and even for existance of computers.
Refer notes/data_categories.png

### Assigment1 given.

## How numbers are stored:

Unsigned Numbers:

The number you should just convert to Binary
For example if the number is 125
1000
1*2(3) + 0*2(2) + 0*2(1) + 0*2(0) = 8
10000 16
100000 32
1000000 64
1100000 64 + 32 = 96
1110000 64 + 32 + 16 = 112
1111101 64 + 32 + 16 + 8 = 125
So when we try to store 125 (a decimal number, i.e. Base-10 number) in Binary, what gets stores is 1111101

When we say the distance from Mys to Blr is 145, what we mean is:
1*10(2) + 4*10(1) + 5\*10(0)
100 + 40 + 5 = 145

So to store 125 we need 7 bits
To store 5 we need 3 bits
To store 20 we need 5 bits.
However, we need disciplene.
Hence we consider
4 bits (Nibble)
8 bits (Byte)
16 bits
32 bits word size
64 bits word size

## Assignment2 give.

In 1 bit we can store how many values?
2 values (0 or 1)
In 2 bits we can store 4 different values
So in n bits we can store 2-power-n values
Thus in 4 bits we can store 16 values, which is 0 to 15 (if unsigned)
16 values are also called as HexaDecimal, 0 to f where f is 15

If signed in 4 bits the values we can store are:
-8 to +7 which is 16 values

## HOW NEGETIVE NUMBERS ARE STORED:

n = -21
Take absolute of the number -21, which is 21
Now convert it to binary
0001 0101

1110 1010 (1s compliment)
1
1110 1011 (2s compliment)
Observe that the MSB (1st from the left) is 1
In signed numbers, the MSB is always sign bit. It tells sign of the number. If MSB is 1, then the number is -ve otherwise +ve.

Thus, how -21 is stored?
11101011
-1 * 2(7) + 1*2(6) + 1\*2(5) + 11
-128 + 64 + 32 + 11
-64 + 43
-21

## Assignment3 given

DataTypes in Java:
Primitive:
Integer Types:
byte 1 byte
short 2 bytes
int 4 bytes
long 8 bytes
Number with precission:
float 4 bytes
double 8 bytes
boolean 1 bit
char 2 bytes (Unicode characters)
reference types (That store reference value of an object)

Datatypes in Python:
int
float
bool
str
chr
Note that in Python, every datatype is of some class. Thus every data in Python is an object.

# OPERATORS:

## Arithmetic Operators:

```
 + - % * /
      ** // (Addition to Python)
```

All Arithmetic operators are binary operators. That is, they need 2 operands/values
The syntax of the language necessitates us to use the operators in INFIX notation (put the operator inbetyween operands)

The compiler (of any language) always compiles the instructions line by line (top to bottom) and each instruction from left to right.
However, the execution machine may not evaluate the instructions or expressions left to right. It may also be right to left.

The Arithmetic expression are by default evaluated from left to right. However, this is overridden by precedence of operators. Thus, the operation with highest precedence is evaluated 1st.

For example,
5 - 6 + 3
Here, 5 - 6 is evaluated 1st. Because the precedence/priority of + and - are same.

4 + 7 / 2
Here, 7/2 is evaluated 1st. and then the quotient is added to 4.

2 ** 3 ** 2
Here, the power operator (w.r.t. Python) has right to left associtivity. Thus the above expression evaluates to 512 and not 64

In Java, to accomplish this, we must use Math.pow()

The I/P to Arithmetic operators are numbers
The O/P is number

Though the we write the expression in Infix notation, the evaluation is done by the execution machine only after converting the infix expression into postfix.

When the operands are of different types the operand with lower sized data type is 1st implicitly converted to the type of the other operand and only then the operation is completed.
5 + 5.5
Here 5.5 is double and 5 is int. Hence, 1st, 5 is converted from int to double

13 + 7
1101
0111

---

DAY3 06-07-2026

W.R.T JAVA:
int num = 40 / 7;
s.o.p(num); // 5

float num = 40 / 7;
s.o.p(num); // 5.0

int num = 40 / 7.0;
s.o.p(num); // 5

Assigment4 given.

## RELATIIONAL OPERATORS:

> < >= <= != ==

I/P are numbers
O/P is boolean
All relational operators are binary
Relational operators have lower precedence than Arithmetic operators, but higher than logical operators.
Note that assignment operator has the least precedence.
The operator having lower precedence than the assignment operator is the post increment or post decrement operator.
num = 5
result = num++;
Here the value of num is assigned to result 1st. And then num is incremented.

Assignment5 given.
Assignment6 given.

Closed Interval
[10, 20] From 10 till 20 (end values are included)
i >= 10 and i <= 20
Open Interval
(20, 40) From 21 till 39 (end value are not included)
i > 20 and i < 40
(15, 25] Left Open. From 16 to 25
i > 15 and i <= 25

for(int i = 1; i <= 10 i++)
for(int i = 1; i < 11 i++)

Assignment7 given:

LOGICAL OPERATORS:
& | ! && ||
In python there are only short circuted operators

I/P are boolean (They are actually outcome of the conditions)
O/P is boolean

int a = 3, b = 5, c = 10;
if (a-- <= b || b++ != c)
print('Mysuru');
else
print('Hunasuru');
print(a, b, c);

int a = 3, b = 5, c = 10;
if (a-- <= b | b++ != c)
print('Mysuru');
else
print('Hunasuru');
print(a, b, c);

int x = 4, y = 5, z = 1;
x++;
s.o.p(x, y, z);
++x;
s.o.p(x, y, z);
y = z++;
s.o.p(x, y, z);
x = ++y;
s.o.p(x, y, z);
z = x++ + ++x;
s.o.p(x, y, z);

Bit Wise Operators:
~ ^ >> << | &

PROBLEM ON BIT WISE OPERATORS (PENDING)

4 + 7 - 2 + 1
x = y

**
3 ** 2

obj1.x_axis p(3, 4)

---

## DAY4 TUESDAY 07-07-2026

int number = 10;
Here the varibale `number` is primitive. That is, it has the only data 10 and nothing else.
int array[10];
Here the `array` w.r.t. C/C++ has 10 int elements and nothing else. Thus, this is also primitive.

int[] array = new int[10];
Here the `array` w.r.t. Java, is not just primitive. But it is an object.

## High Cohesion (SRP)

One Solution must solve only one problem at a time.
Do One job at a time.

`SOLID Principles`

int number; // generic information
int age; // specific information
int student_age; // specialized information

class StudentAge {
int age;
int maxAge;
int minAge;
}

StudentAge vtu_age; 18 and 60
StudentAge jntu_age; 16 and 80

---

1. Check if a year is Leap year
2. Find if a number is Perfect Square
3. Accept the average score from the user and print the result as follows:
   0 to 49 Fail
   50 to 69 Second Class
   70 to 89 First Class
   90 to 100 Distiction

## STEPS TO SOLVE A PROBLEM:

### 1. Understand the problem. Isolate/Remove the unwanted information. Unambigiously assertain the I/P Data and recognise what is the O/P Data. Also remember the relevant/important information.

### 2. Build the solution. Using trail and error method or using any specific algorithm or formula. But never using any programming concepts.

### 3. Write the Algorithm. Step by step procedure.

Each step must be finite, simple and unambigious and must follow SRP.

### 4. Write the fake code (pseudocode).

### 5. Code it

### 6. (OPTIONAL) Validate/test/verify the pseudocode. Also check if there can be a better solution by examining the efficiencies. Lastly see if the code/solution can be optimized.

Assignment8 given.

Machine Language
Human friendly language (assembly language)
Domain Oriented languages (Cobol, Fortran)
There were only domain oriented languages.
Domain friendly languages (C, Pasacal)
OOPL (C++, C with classes, Simula67)

C++ = C + OO
Used inheritance to give the increment OO concepts to C and thus C++ came into existance.

Thus every C program is also a C++ program. But the other way is not correct.
Because C++ is super set and C is sub set of C++

C++ had some flaws (friend, inhetir by private, global variables and functions, operatr overloading, objects in Stack area)
For the above issues, experts wanted a Strict OOPL
Thus Java was introduced.

Assignment9 given.
Assignment10 given.
Assignment11 given.

---

DAY7 THURSDAY 09-07-2026

Formatting the output is taught.
Assignment12 given.

---

DAY8 FRIDAY 10-07-2026
Functions
Call Stack
PDB
match-case
Problem solving on Loops/iterations
range function with yield

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l1.extend(l2)
print(len(l1)) # 10
print(l1) # [1,23,4,5,6,7,8,9,0]

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]
l1.append(l2)
print(len(l1)) # 6
print(l1) # [1,2,3,4,5, [6,7,8,9,0] ]
l1[5][2]

i = -1
i -= -1
i -= x
i = i - x
i = i - (-1)
i = -1 +1
i = 0

Find sum of Even digits of a number

```
n = int(input())
sum_of_even_digits = 0
while n != 0:
  digit = n % 10 # extract digit at one's place
  if digit % 2 == 0:
    sum_of_even_digits += digit
print(sum)
print(digit) # NameError
```

Find sum of Even Placed digits
n = 2354615 # odd number of digits
n = 4576 # even number of digits
flip = True
If flip remains True after completion of the loop, then the number has even number of digits.

```
sum1 = 0
sum2 = 0
flip = True
while n != 0:
  digit = n % 10
  n = n // 10
  if digit % 2 == 0:
    if flip:
      sum1 += digit
    else:
      sum2 += digit
  flip = not flip # !flip
if !flip:
  print(f'Sum of Odd placed Even digits is {sum1}')
else:
  print(f'Sum of Odd placed Even digits is {sum2}')
```

## Functions:

Functions are used to implement a small piece of logic/algorithm. A function must exhibit SRP (high cohesion)
A function may receive arguments
A function may return acknowledgement or result.
For example, sqrt() returns result
prinft() in C returns acknowledgement.

---

DAY8 MONDAY 13-07-2026
FUNCTION CALL STACK

Special Purpose Registers:
IR: Instruction Register
It stores address of the instruction that is getting executed
PC: Address of the next instruction to be executed is stored in Program counter
FP: Frame Pointer
It holds address of the the frame of the function that is currently getting executed
SP: Stack Pointer
It holds address of the top frame in the Stack
FRAME: A frame is memory allocated to a function during runtime. It has 4 data in it.

1. The function parameters
2. The local variables
3. return address
4. Addresses of the called functions
   MDR
   MAR
   Accumalator: It is used to store intermediate results with in the same statement.

---

def goa():
print('I came to enjoy the beaches')
mumbai('good vibes')
print('I came to goa to enjoy the Cruise')

def mumbai(param):
print('I came to Mumbai to learn Stck Markets')
vadodara()
print('I came back to Mumbai to enjoy the Vada Paav')

def vadodara():
my_age = 40
print('I came to Vadodara to enjoy India's 1st Bullet train and to buy Diamonds')

print('I am at home')
goa() # address of goa function 675
print('I am back home')

---

main() should call run_app()
run_app() calls run_menu()
run_menu() takes the choice from run_app() and runs that functionality as per choice.
For every choice the user makes and that functionality has run, the menu should be displayed again until the user whishes to quit the App.

---

DAY9 TUESDAY 14-07-2026

## DATA STRUCTURES:

int num1 = 0, num2 = 0, num3 = 0;

num3 This gives value of num3
&num3 This gives address of num3
&num3 + 1 `This gives address of next integer value in memory. That might be num2 (We are making a blind and dangerous assumption here)
\*(&num3+1) Here we get the value of num2

int n1 = 0, n2 = 0, n3 = 0, n4 = 5, n5 = 10;
int n1, n2, ..... n50;
int numbers[500];
Using index we can differentiate all 500 variables in `numbers`
The index starts from 0 and goes upto n-1 where n is the size/length of the array.
Here, all the 500 variables/values are stored in contigious memory locations. That is, there is no gap in between any 2 consecutive elements/values.

1st element in the array is accessed as numbers[0]
mth element in the array is accessed as numbers[m-1]
So, we can access any element in the array randomly. i.e., without use of itearations. Thus accessing (LookUp) an element in an array is One unit time. Thus the efficiency is O(1)
Thus an Array is time efficient Data Structure.
Array is an memory inefficiecnt DS.

prompt/input/scanf/cin The `size`

```
float *ptr = new float[size];
float[] array = new float[size];
```

class Node:
def **init**(self, data = ''):
self.data = data
self.link = None

class LinkedList:
def **init**(self):
self.head = None

    def insert(self):
        pass

    def delete_node(self):
        pass

    def update(self):
        pass

    def search(self, element = '')
        pass

    def list(self):
        pass

---

DAY10 15-07-2026 WEDNESDAY

Linear Search
Binary Search.
Insertion Sort
Quick Sort
Heap Sort
Merge Sort
Bucket Sort
Redox Sort
Radix Sort (Non comaparison sorting)

---

DAY12 18-07-2026 SATURDAY

- Briefly describe how the algorithm works. Use Simulation/Visualization
- Now Write the algorithm. Step by Step procedure. Discuss the strategy (divide and conquer or brute force etc.)
- Write the Pseudocode
- Now discuss different possibilities (I/P data structure is Almost sorted, fully sorted, randomly sorted, small in size, big in size and combinations)
- Thus discuss the efficiencies (Mathematically)
- Use Flow chart to make them understand the debugging
- Optimization techniques
- Code it! (Imeplement) This is the only step where we talk about programming or the language
- Application(s) of the algorithm
- Comparison with its peers.

(n-1) + (n-2) + (n-3) + ..... 3 + 2 + (n - (n - 1))
= n2 -2n + 1
= O(n2)

array = 23 45 4 21 77 10 15

for i from 1 to N-1 do: // for each element in unsorted array
element = array[i] // element to be inserted
j = i - 1
while element < array[j] and j >= 0:
array[j+1] = array[j]
j--
array[j+1] = element

[0, k] is the number of shifts where k is number of elements in the sorted array.

---

## Binary Search

do while loop

Pre requisite: Array must be sorted and also we must the order in which it is sorted.

We go to mid of the element (median) and check if it is the search element.
If yes , everything fine we got the element.

Note that by reaching the mid element we have divided the array in 2 equal halves.

Otherwise check if the element is in 1st half (left half) or 2nd half of the array.
Accordingly set the search array as 1st or 2nd half.

101
51st element is the search element.
Thus 51 elements are eleminated from the search area.

Possibilities:
Best case scenario:
The element might be the exact mid element of the given array. Thus the number of searches is 1. So, the BCE of Binary search is O(1)

1. Element not found
   1. search element smaller than the 1st element.
   2. search element bigger than the last element.
   3. Search element is in between consecutive 2 elements of the array.

2. Element found:
   1. Mid element of the given array
   2. 1st element
   3. Last element
   4. In between element.

array = [some elements]
low  = 0  // index of 1st element
Read search_element
high = N-1 // N is size of array.
do
  mid = (low + high) // 2 # Integer division
  if arrayt[mid] == search_element then:
    return mid as index of search_element
  else if search_element < array[mid] then:
    high = mid - 1
  else:
    low = mid + 1
while low <= high;


Worst case efficienfy of Binary Seacrh:

The efficiency depends on number of iterations of the loops in the algorithm.
Since we dont know the number of iterations in Binary search, because we are using while or do-while loop, we assume it to be X

In 1st iteration, number of elements is N
Thus, in consecutive iterations, the number of elements are:

N     N/2     N/4     N/8      ......     8      4      2       1
2(X-1)                                            2(2)   2(1)   2(0)

N = 2 pow X-1
N = 2^X
X = LogN

100000
50000
25000
12500
6250
3125
1562
731
365
182
91
45
22
11
5
2
1
