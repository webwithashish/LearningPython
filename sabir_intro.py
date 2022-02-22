# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd lesser_of_two_evens(2,4) --> 2 lesser_of_two_evens(2,5) --> 5
num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
"""if num1 % 2 == 0 and num2 % 2 == 0:
    if num1 < num2:
        print(num1)
    else:
        print(num2)
elif num1 % 2 != 0 or num2 % 2 != 0:
    if num1 > num2:
        print(num1)
    else:
        print(num2)
else:
    print("invalid input")"""


def comp(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    return max(num1, num2)


print(comp(num1, num2))
