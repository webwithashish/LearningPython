class A:
    a = 100

    def displayA(self):
        print(f"value of a is {self.a}")


class B:
    b = 200


class C:
    c = 300


class D(A, B, C):
    def sum(self):
        print(self.a + self.b + self.c)
        self.displayA()


z1 = D()
z1.sum()
