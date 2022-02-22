# greater number in three
# take three input from user find out the greatest amoung those

a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))
if a > b and a > c:
    print(a, "the first number is greater ")
elif b > a and b > c:
    print(b, "the second number is greater ")
elif c > a and c > b:
    print(c, "the third number is greater")
elif a == b == c:
    print("all numbers are same ")
else:
    print("two numbers are same")
