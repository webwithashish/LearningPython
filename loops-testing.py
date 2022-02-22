name = "abc pqr abc abc"

"""flag = 0
for n in name:
    if n == "a":
        flag = 1
if flag:
    print("prsennt")
else:
    print("not")"""

# for n in name:
#     # print(n)
#     if n == "r":
#         print("present")
#         break

"""i = 0
for t in name:
    if t == "a":
        i = i+1
print(i)
"""
"""nums=[num for num in range(0,11) if num%2==0]
print(nums)"""

nums = [num if num % 2 == 0 else 'ODD' for num in range(0, 21)]
print(nums)

"""celcius = (0, 12, 14, 50, 132)
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(f"in far{fahrenheit}")"""
