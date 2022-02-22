# printing the value given by user
# supp = 1
# start = int(input("enter the start value"))
# end = int(input("enter the end value"))
# num = range(start, (end+supp))
# for x in num:
#     print(x)

# step of 4
# num1 = range(7,30,4)
# for i in num1:
#     print(i)

# num2 = range(1, 30)
# for i in num2:
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

# 1 to 5 print te addition
# num3 = range(6)
# sum = 0
# for i in num3:
#     sum = sum + i
# print(sum)

num4 = range(1, 11)
sumEven = 0
sumOdd = 0
for i in num4:
    if i % 2 == 0:
        sumEven = sumEven + i
    else:
        sumOdd = sumOdd + i
print("the sum of even numbers: ", sumEven)
print("the sum of odd numbers: ", sumOdd)

