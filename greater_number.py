# take two numbers from user and check which one is greater amoung

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
if num1==num2:
    print(" entered numbers are equal ")
elif num1>num2:
    print(num1," is greater than " ,num2)
elif num2>num1:
    print(num2,"is greater than ",num1)
else:
    print("invalid input")