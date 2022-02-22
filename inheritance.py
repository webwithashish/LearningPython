"""class Parent:
    a = 100
    b = 200

    def mul(self):
        print(self.a * self.b)


class Child(Parent):

    def add(self):
        print(self.a + self.b)


c1 = Child()
c1.add()
c1.mul()"""
from Tools.scripts.dutree import display

"""class parent:
    last_name = "latake"


class child(parent):
    name = "ashish"

    def display(self):
        print(f"welcome {self.name} {self.last_name}")


e1 = child()
e1.display()"""

"""class GrandParent:
    a = 100


class Parent(GrandParent):
    b = 200

    def add(self):
        print(self.a + self.b)


class Child(Parent):
    c = 50

    def add(self):
        print(self.a + self.b + self.c)


p1 = Parent()
p1.add()
c1 = Child()
c1.add()"""


class Person:
    name = "ashish"
    city = "Barshi"
    contact_no = 9834268459


class Lecture(Person):
    taking_subject = "web Scraping"


class GuestLecture(Lecture):
    remuneration_per_batch = 1000
    batches_num = 3

    def payment(self):
        print(
            f"{self.name} {self.contact_no} {self.city} total amount {self.remuneration_per_batch * self.batches_num}rs")


d1 = GuestLecture()
d1.payment()
