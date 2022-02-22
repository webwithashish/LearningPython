"""class Parent:
    def __init__(self, surname):
        self.surname = surname


class Child(Parent):
    def __init__(self, name, surname):
        self.name = name
        super().__init__(surname)

    def show(self):
        print(self.name, self.surname)


C1 = Child("ashish", "latake")
C1.show()"""


class parent:
    a = 100

    def display(self):
        print(self.a)


class child(parent):
    a = 50
    b = 100

    def add(self):
        print(super().a)
        print(self.a + self.b + super().a)
        print(super().a)


c1 = child()
c1.add()
