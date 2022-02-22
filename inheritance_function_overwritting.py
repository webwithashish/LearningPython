class Shape:
    def drawshape(self):
        print("draw shape")


class Square(Shape):
    def drawshape(self):
        print("this will draw square")


class Circle(Shape):
    def drawshape(self):
        print("this will draw circle")


class Rectangle(Shape):
    def drawshape(self):
        print("this will draw Rectangle")


s1 = Square()
r1 = Rectangle()
c1 = Circle()
s1.drawshape()
r1.drawshape()
c1.drawshape()
