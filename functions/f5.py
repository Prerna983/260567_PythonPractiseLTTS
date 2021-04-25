def square(x):
    return x * x


def test(func, x):
    print(func(x))


test(square, 4)
test(square, 42)
test(square, 50)
