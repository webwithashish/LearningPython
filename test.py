# Python program to check if the number is an Armstrong number or not

"""# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")"""

"""name = "bharti dutta"
i = 0
while i < len(name):
    if (i + 1) % 3 == 0:
        print(name[i], i + 1)
    i += 1"""
"""w = input("Van")
s = 0
for x in w:
    s = s + ord(x)
    print(1)
n = s
print("this is ", n, s)
c = 0
while n > 0:
    n = n // 10
    c = c + 1
n = s
r = 0
while n > 0:
    d = n % 10
    n = n // 10
    r = r + d ** c
a = ""
if s == r:
    for x in w:
        if x not in a:
            a = a + x
    print(a)
else:
    print(-1)"""

"""SPY
GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
spy_game([1, 2, 4, 0, 0, 7, 5]) --> True
spy_game([1, 0, 2, 4, 0, 5, 7]) --> True
spy_game([1, 7, 2, 0, 4, 5, 0]) --> False"""
"""def spy_game(nums):
    check = [0, 0, 7, 'a']

    for num in nums:
        if num == check[0]:
            check.pop(0)

    return len(check) == 1"""
"""def spy_game(lst):
    check = [0, 0, 7]
    ci = 0
    for i in lst:
        if ci == 2:
            return True
        elif i == check[ci]:
            ci += 1
    else:
        return False"""
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
"""n = int(input("enter the number"))
for i in range(n):
    print(i + 1, end="")"""

"""value = 1
mylist = []
while value < 11:
    num = int(input(f"enter {value} the number "))
    value += 1
    mylist.append(num)

rvsdlst = mylist[::-1]
print(f"original list {mylist}")
print(f"reversed list {rvsdlst} ")"""

"""
Q) Take 10 integer i/p from user.print the following

1.No.of positive numbers

2.no.of negative numbers

3.no.of odd numbers

4.no.of even numbers

5.no.of zeros
"""
"""value = 1
mylist = []
while value < 11:
    num = int(input(f"enter {value} the number "))
    value += 1
    mylist.append(num)

evencount = 0
oddcount = 0
positivecount = 0
negativecount = 0
zerocount = 0
for i in mylist:
    if i == 0:
        zerocount += 1
        continue
    if i % 2 == 0:
        evencount += 1
    else:
        oddcount += 1
    if i > 0:
        positivecount += 1
    else:
        negativecount += 1

print(f"number of zeros {zerocount}")
print(f"number of even numbers {evencount}")
print(f"number of odd numbers {oddcount}")
print(f"number of positive numbers {positivecount}")
print(f"number of negative numbers {negativecount}")"""

"""num = input("enter the number ")
lnth = len(num)
num = int(num)
print(f"{num} this number has {lnth} digit")"""

"""# name id age dept salary
# revise the salary
# add company name and address
# remove the age
employee = {"name": "ashish", "id": 101, "age": 22, "department": "web dev", "salary": 67890}
print(employee)
employee["salary"] *= 12
print(employee)
employee["company"] = "ipsum"
print(employee)
employee["address"] = ["pune", "solapur"]
print(employee)
employee.pop("age")
print(employee)"""

"""str = input("enter a string ")
# if str[0].isdigit():
if int(str[0]):
    print(f"string is starting with digit {int(str[0])}")
else:
    print("string is not starting with digit")"""

"""print("Enter a String: ", end="")
text = input()
for char in text:
    ascii = ord(char)
    print(char, "\t", ascii)"""

"""lst = [1, 2, 3, 2, 42, 5, 2, 52, 423, 51, 1, 23, 4, 2, 3]
result = set()
for i in lst:
    result.add(i)
print(result)
print(sorted(result))"""

# ----------------------------------------------------------------------------------------------------------
# class test number 2
# question number 1
"""class comp:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def great(self):
        print(f"{max(self.num1, self.num2)} is a greater number")


n1 = comp(234, 142)
n1.great()
n2 = comp(23, 42)
n2.great()"""
# Write a program to print the sum of digits of entered number
"""num = input("enter a number ")
sum = 0
for i in num:
    sum += int(i)
print(f"the sum of the digits of entered number is {sum}")"""

# Write a program to check the entered character is vowel or not
"""char = input("enter a character ")
if char.lower() in ["a", "e", "i", "o", "u"]:
    print("entered character is vowel")
else:
    print("entered character is not vowel(consonant)")"""

# Write a program to print the sum of entered numbers
"""num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
print(f"sum of entered numbers is {num1 + num2}")"""

# Write a program to print how many zero and how many non zero values are present in a list of 10 entered integer values
"""incount = 1
numlst = []
while incount <= 10:
    num = int(input("enter a number "))
    numlst.append(num)
    incount += 1
count_zero = 0
for i in numlst:
    if i == 0:
        count_zero += 1

print(f"zero values entered = {count_zero}")
print(f"non zero values entered = {10 - count_zero}")"""

# how to overridden function in derived classes
"""class Book:
    # function in the base class
    def printbook(self):
        print("printing a book")


class Alchemist(Book):
    # overridden function in derived class for printing alchemist book
    def printbook(self):
        print("alchemist book is being printed")


class Mindset(Book):
    # overridden function in derived class for mindset book
    def printbook(self):
        print("mindset book is being printed")


b1 = Alchemist()
b2 = Mindset()
b1.printbook()
b2.printbook()"""
# write a program to find out entered number is palindrome or not
"""
num = input("Enter a number")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")"""
"""test_number = int(input("enter a number to check palindrome"))
print("The original number is : " + str(test_number))
res = str(test_number) == str(test_number)[::-1]

if res:
    print("entered number is palindrome")
else:
    print("entered number is not palindrome")"""

"""#  write a program to find out entered number is palindrome or not
# what is palindrome
# 12321,121,232,1234321
# if you read this number from start to end and ending to the start

# step1 : take number from input
check_num = int(input("enter a number to check palindrome "))
# step 2: reverse the input number and store it in a variable(we have to convert a number to a string)
rsvd_num = str(check_num)[::-1]
# checking for palindrome
# check_num is int type and we have to convert rsvd_num to int as well to do a comparison in those same
if check_num == int(rsvd_num):
    # if the entered number(ckeck_num) is same as revered number (rsvd_num) then its palindrome number
    print("entered number is palindrome")
else:
    # if entered number is not same as reversed number then its not palindrome
    print("entered number is not palindrome")
"""
