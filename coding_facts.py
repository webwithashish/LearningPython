count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"we have {count} even numbers")

# print the square root of the number
number = 25
square_root = number ** 0.5
print(int(square_root))

# swapping of two variable
"""a = 20
b = 10
print(f"a={a},b={b}")
swap = a
a = b
b = swap
print(f"a={a},b={b}")"""

# different method (with built in method)
a = 5
b = 7
print(f"before a= {a} and b={b}")
a, b = b, a
print(f"after a= {a} and b={b}")

# print 7 times "hello"
for i in range(1, 8):
    print(f"{i}hello")
