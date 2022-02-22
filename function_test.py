# take two number form user ask for users choice for performing the operation on it
# done this by using functions

def add(num1, num2):
    output = num1 + num2
    return output


def sub(num1, num2):
    output = num1 - num2
    return output


def mul(num1, num2):
    output = num1 * num2
    return output


def div(num1, num2):
    output = num1 / num2
    return output


a = int(input("enter the first number "))
b = int(input("enter the second number "))
print("for addition enter 1 \nfor subtraction enter 2 \nfor multiplication enter 3 \nfor division enter 4")
choice = int(input("enter your choice "))
if choice == 1:
    print(f"the output is {add(a,b)}")
elif choice == 2:
    print(f"the output is {sub(a, b)}")
elif choice == 3:
    print(f"the output is {mul(a, b)}")
elif choice == 4:
    print(f"the output is {div(a, b)}")
else:
    print("invalid user choice")
