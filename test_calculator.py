# encoding: utf-8


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    return -1


def test_add():
    assert add(1, 2) == 3


def test_div():
    assert div(5,0)==-1


if __name__ == '__main__':
    # print(add(5, 8))
    pass
