class Base:
    __a = 100  # this is private variable only available in the class and its own objects

    def show(self):
        print(self.__a)


"""class Driven(Base):
    def display(self):
        print(super().__a)"""

b1 = Base()
print(b1.__a)
b1.show()
"""b2 = Driven()
 b2.display()
b2.show()"""
