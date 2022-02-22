from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        print("Drawing a shape")

    def display(self):
        print("display function")


class Square(Shape):
    def draw(self):
        print("draw square")


class Rectangle(Shape):
    def draw(self):
        print("draw rect")


class Circle(Shape):
    def draw(self):
        print("draw circle")


s1 = Square()
r1 = Rectangle()
c1 = Circle()

s1.draw()
r1.draw()
c1.draw()
# r1.display()
# help(s1.draw)
