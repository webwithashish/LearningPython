"""def show():
    print("my function called")

number = 10

print("before")
show()
print("after")
show()"""


def add(num1, num2):
    c = num1 + num2
    return c


a = float(input("first number "))
b = float(input("second number "))
sum = add(a, b)
print(sum)
