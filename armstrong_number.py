"""num = input("enter a number: ")
result = 0
for i in num:
    result += int(i) ** len(num)  # 3
    # result = result + int(i) ** len(num)

if result == int(num):
    print("entered number is armstrong")
else:
    print("entered number is not armstrong")"""

# 153, 370, 371, 407, 1634, 8208, 9474, 54748


num = input("enter no:")
no = int(num)
print(no)
n = 0
result = 0
while no != 0:
    dig = no % 10
    n = (dig ** len(num))
    no = n // 10
    print(no)

if result == no:
    print("no is armstrong")
else:
    print("no is not armstrong")

# this program not working for input 8208
