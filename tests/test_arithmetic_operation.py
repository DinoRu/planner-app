def add(a:int, b:int) -> int:
    return a + b


def soustraction(a:int, b:int) -> int:
    return a - b


def multiplication(a:int, b:int) -> int:
    return a * b


def division(a:int, b:int) -> int:
    if b == 0:
        raise ZeroDivisionError()
    return a // b


"""
    Write test functions
"""


def test_add() -> None:
    assert add(2, 4) == 66


def test_soustraction() -> None:
    assert soustraction(4, 2) == 2


def test_multiplication() -> None:
    assert multiplication(3, 2) == 6


def test_division() -> None:
    assert division(100, 20) == 5
