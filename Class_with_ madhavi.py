# f.string (formatted string literal)
# .format method
# shortcuts
# Data types
# some coding problems
# keyboard shortcuts HOME, END, shift+enter, alt+ shift+ arrow_keys, ctrl+D


"""name = input("enter your name ")
age = int(input("enter your age "))
# hello [ashish] your age is 22
print("hello[" + name + "] your age is", age)
# print("hello {} your age is {}".format(name, age))
print(f"Hello [{name}] your age is {age}")"""

""""# Q) read a number from user and count the no.of digits present in the i/p number
# 1 question must in front of you
# 2 divide that question in small tasks

# step 1 taking input from user
# step 2 count the length of number"""

# first take a number from user
# if the number is completely divisible by 3 print FIZZ
# if the number is divisible by 5 print BUZZ
# if the number is divisible by both 3 and 5 print FIZZ-BUZZ
# any other number just print the number as it is

"""number = int(input("enter the number "))

if number % 3 == 0 and number % 5 == 0:
    print("FIZZ-BUZZ")
elif number % 3 == 0:
    print("FIZZ")
elif number % 5 == 0:
    print("BUZZ")
else:
    print(number)"""
# what continue does --> it goes to closet enclosing loop
# what break does --> it breaks out of closet enclosing loop
# what pass does --> it does nothing (placeholder)


"""nums = range(1, 21)
even_count = 0
odd_count = 0
for num in nums:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(f"even count {even_count}")
print(f"odd count {odd_count}")"""

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

"""def checkeven(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    return max(num1, num2)


print(checkeven(2, 4))
print(checkeven(2, 5))
print(checkeven(3, 7))
print(checkeven(10, 20))
print(checkeven(4, 13))"""

"""number_list = "snake casing"
NumberList = "camel casing"
com = 3 + 6j
print(com)
print(type(com))"""

"""# program to find prime number
num = int(input("enter a number "))  # step 1

if num == 1:
    print("its not prime number ")

else:
    for i in range(2, num):
        if num % i == 0:
            print("not a prime number")
            break

    else:
        print("it's a prime number")  # step 2"""

"""# for else loop exe
nums = [1, 3, 6, 7, 10, 11]
for i in nums:
    if i % 2 == 0:
        print(f"{i}even number present in the list")
        break
else:
    print("no even numbers in the list")"""

# greater in three
"""a = int(input("enter a number "))
b = int(input("enter a number "))
c = int(input("enter a number "))
if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")"""

"""a = 10
b = 20
temp = a  # temp = 10
a = b  # a = 20
b = temp  # b = 10
print(a)
print(b)"""
"""a = 10
b = 20
print(a)
print(b)

a = a + b  # a = 30
print(f"first step {a}")
b = a - b  # b(10) = 30 - 20
print(f"second step {b}")
a = a - b  # a(20) = 30 - 10

print(a)
print(b)"""

"""ch = input("enter a char ")
# if ch.lower() in ["a", "e", "i", "o", "u"]:
# if ch.upper() in ["A", "E", "I", "O", "U"]: # list
# if ch.upper() in ("A", "E", "I", "O", "U"): # tuple
# if ch.upper() in {"A", "E", "I", "O", "U", "U"}:  # set

if ch.upper() in "A" "E" "I" "O" "U":
    print("it is a vowel")
else:
    print("its a consonant")"""
