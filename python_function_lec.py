"""def add(x, y=20, z=30):
    print(x + y + z)"""

# add(1, 2, 3)
# add(1)
# add(2, 3)


"""def great(*args):
    max_num = 0
    for i in args:
        if i > max_num:
            max_num = i
        else:
            pass
    return max_num


print(great(12, 423, 435, 6476, 23, 2234))"""

"""def func(*arg):
    for i in arg:
        i += i

    print(i)


# display(10)
# display(12,67,89)
func(12, 45, 67, 89, 67)"""

# wap to compare two lists are same or not?
"""def comp(*args):
    if len(args[0][0]) == len(args[1][0]):
        if args[0] == args[1]:
            print("lists are same")
        else:
            print("lists are not same")
    else:
        print("lists are not same and list length is also different")


l1 = ["ashish"]
l2 = ["abhishek"]

comp(l1, l2)"""

"""def com(l1, l2):
    i = len(l1)
    j = len(l2)
    if i == j:
        flag = 0
        x = 0
        while x < i:
            if l1[x] != l2[x]:
                flag = 1
                break
            x = x + 1
        if flag == 0:
            print("same")
        else:
            print("not")
    else:
        print("not of same length")


l1 = [20, 7, 80]
l2 = [20, 7, 80]
com(l1, l2)"""


def comp(l1, l2):
    if len(l1) == len(l2):
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                flag = True
            else:
                flag = False
                break
        if flag:
            print("the list is same")
        else:
            print("the list is not same")
    else:
        print("the list length is not same")


l1 = [12, 13, 34, 45]
l2 = [12, 13, 34, 45]
comp(l1, l2)
