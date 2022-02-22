def smartsub(sub):
    def inner(x, y):
        if x < y:
            # x, y = y, x
            return sub(y, x)
        else:
            return sub(x, y)

    return inner


@smartsub
def sub(x, y):
    print(x - y)


sub(10, 3)
sub(3, 10)
