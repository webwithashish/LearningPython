# take two numbers from user and also take a choice of action to perform on those same print the result

num1 = int(input("enter your first number "))
num2 = int(input("enter your second number "))
output = 0
choice = input("enter your choice \n + for add, - for sub, * for multi, / for div \n ")

if choice == "+":
    output = num1 + num2
    print(output, "this is the addition for entered number")
elif choice == "-":
    output = num1 - num2
    print(output, "this is the SUB for entered number")
elif choice == "*":
    output = num1 * num2
    print(output, "this is the multiplication for entered number")
elif choice == "/":
    output = num1 / num2
    print(output, "this is the division for entered number")
else:
    print("invalid choice input")
