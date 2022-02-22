class Parent:
    a = 100

    def display(self):
        print(self.a, "base class display")


class ChildFunction(Parent):
    def display(self):
        print("derived class dispaly")

    def show(self):
        self.display()
        super().display()


e1 = ChildFunction()
# e1.display()
e1.show()
