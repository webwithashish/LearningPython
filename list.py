# list1 = [4, 12, 1999]
# print(type(list1),list1 )

# list2 = ["text", "text2", "text3"]
# print(type(list2), list2)

# list3 =[123.45, 12, "string"]
# print(type(list3), list3)
# print(list3[0:2])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list[3])
# print(list[2:7])
# print(list[-4])
# print(list[-5:-2])

# list[3] = 900
# list[4:5]=[456,45,789]
# list.reverse()
minE = min(list)
print("min element:", minE)
maxE = max(list)
print("max element:", maxE)
list.append(11)
print("appended list:", list)
list.pop()
print("after pop(): ", list)
list.insert(3, 3000)
print("inserted list:", list)
list.sort()
print("sorted list:", list)
list.reverse()
print("reversed list:", list)
# list.clear()
print("sum of list", sum(list))
print(list.count(3000))
list.remove(3000)
l1 = [41, 42, 43]
list.extend(l1)
print(list)
lorem = list.pop(3)
print(lorem)
# lorem = list.remove(3)
