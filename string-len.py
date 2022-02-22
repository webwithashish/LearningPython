# take a string and find out the length of the string without using the len function

string = "Hello World"
"""i = 0
for _ in string:
    i = i+1
print("\nthe lenght with the loop:", i)

print("the actual length of the string:", len(string))"""

i = 0
nums = [i for i in string]
print(nums)