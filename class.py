"""class Emp:
    def getData(self, id1, name1, salary1):
        self.id = id1
        self.name = name1
        self.salary = salary1

    def display(self):
        print(self.id, self.name, self.salary)


e1 = Emp()
e2 = Emp()
e1.getData(101, "dff", 34555)
e2.getData(102, "gtgt", 89090)
e1.display()
e2.display()"""

"""class student:
    def getdata(self, roll_no1, name1, marks1):
        self.roll_no = roll_no1
        self.name = name1
        self.marks = marks1

    def display(self):
        print(self.roll_no, self.name, self.marks)

    def result(self):
        print(self.marks)


s1 = student()
s2 = student()
s1.getdata(101, "ashish", 87)
s2.getdata(102, "akshay", 98)
if s1.marks > s2.marks:
    s1.display()
else:
    s2.display()"""


class books:
    def getdata(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


b1 = books()
b2 = books()
b3 = books()
b1.getdata(111, "alchemist", 500)
b2.getdata(222, "atomic habits", 794)
b3.getdata(333, "keller", 1268)
print((b1.price + b2.price + b3.price) / 3)
