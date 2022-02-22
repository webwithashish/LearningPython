"""# this is division by zero execption handling
a = 10
b = 2
try:
    c = a / b
except Exception as a:
    print(a)
    print("you can not divide a number by zero")
else:
    print(c)
finally:
    print("final code")
print("rest code")
"""

"""# this is list index out of range exception handling
l1 = [45, 78, 89]
i = 4
try:
    print(l1[i])
except Exception as m:
    print(f"{m} ----this is except suite")

else:
    print(f"{l1} this is else suite")
finally:
    print("this is finally suite")
print("rest of the code here")
"""

# this is name is not defined exception handling
"""try:
    print(a)
except Exception as m:
    print(f"{m} ----- this is except suite")
else:
    print("this is else suite")
finally:
    print("this is finally suite")
print("rest of the code")"""

"""import os

print(os.getcwd())  # this is used to check the current working directory
# print(os.listdir('d://#Full stack developer//#PROGRAMMING TECH//Python//video lects'))
# os.mkdir('foldercreated') # this is used to create a new folder in the same directory
# os.mkdir('FAV FOLDER FOR TEST') # another folder created in the same directory
# for removing the folder we use os.rmdir('FAV FOLDER FOR TEST')method
# os.rmdir('FAV FOLDER FOR TEST')
print(os.listdir("c://Users//ashis//PycharmProjects//Hello_world"))"""

"""a = 11
if a <= 10:
    print("a is less than or equal to 10")
else:
    print("a is greater than 10")"""

"""# factorial of a number
# 5! = 5*4*3*2*1 = 120
num = int(input("enter a number "))
result = 1
for i in range(1, num + 1):
    result *= i

print(f"the factorial of number {num} is {result}")"""
