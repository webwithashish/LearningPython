"""class Employee:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def display(self):
        print(self.id, self.name, self.age)


e1 = Employee(101, "bharti", 23)
e2 = Employee(102, "dutta", 20)
e1.display()
e2.display()"""


class comp:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def great(self):
        print(f"{max(self.num1, self.num2)} is a greater number")


n1 = comp(234, 142)
n1.great()
n2 = comp(23, 42)
n2.great()

import datetime

# print(datetime.datetime.now().strftime("%d\t%A\t%w"))
