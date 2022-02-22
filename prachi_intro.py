# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
#
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

"""num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))


def comp(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    return max(num1, num2)


print(comp(num1, num2))"""

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

"""prachi = 'Crazy Cangaroo'


def f1(str):
    sub_str = str.lower().split()
    if sub_str[0][0] == sub_str[1][0]:
        return True
    return False


# result = f1('Levelheaded Llama')
result = f1(prachi)
print(result)"""

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20
# or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

"""num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))


def check_sum(num1, num2):
    if num1 == 20 or num2 == 20:
        return True
    elif sum([num1, num2]) == 20:
        return True
    return False


print(check_sum(num1, num2))"""

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

"""def cap(str):
    str1 = str[:3]
    # print(str1)
    str2 = str[3:]
    # print(str2)
    return str1.capitalize() + str2.capitalize()


print(cap('macdonald'))"""

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

"""def rvsd(str):
    splt_str = str.split()
    # print(splt_str)
    rsd_str = splt_str[::-1]
    # print(rsd_str)
    final_str = ' '.join(rsd_str)
    # print(final_str)
    return final_str


print(rvsd('I am home'))"""

"""def masteryoda(text):
    newSentence = []
    text.split()
    for x, c in enumerate(text):
        if x == -1:
            newSentence.insert(0, c)
        elif x == 0:
            newSentence.insert(-1, c)
        else:
            newSentence.insert(1, c)
    newerSentence = newSentence.join()
    print(newerSentence)


masteryoda('I am home')"""

"""str = "prachi"
sub_str = str[::-1]
print(sub_str)"""

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

"""num = int(input("enter the n "))


def prachi(n):
    if n in range(1, 111) or n in range(200, 211):
        return True
    return False


print(prachi(num))"""


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def doll(str):
    final_str = []
    for letter in str:
        final_str.append(letter * 3)
    return ''.join(final_str)


print(doll("Hello"))

"""num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in num:
    print(i)"""
