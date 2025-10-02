import pytest

from calculator import Calculator


def test_add_one_plus_one_gives_two():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 1
    number2 = 1
    expected_answer = 2

    # act
    actual_answer = calc.add(number1, number2)
    # assert
    assert actual_answer == expected_answer


def test_add_one_plus_two_gives_three():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 1
    number2 = 2
    expected_answer = 3

    # act
    actual_answer = calc.add(number1, number2)
    # assert
    assert actual_answer == expected_answer


def test_add_one_plus_ten_gives_eleven():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 1
    number2 = 10
    expected_answer = 11

    # act
    actual_answer = calc.add(number1, number2)
    # assert
    assert actual_answer == expected_answer


#     edge cases / boundary values
def test_add_one_plus_minus_one_gives_zero():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 1
    number2 = -1
    expected_answer = 0

    # act
    actual_answer = calc.add(number1, number2)
    # assert
    assert actual_answer == expected_answer


def test_subtract_two_takeaway_one_gives_one():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 2
    number2 = 1
    expected_answer = 1

    # act
    actual_answer = calc.subtract(number1, number2)
    # assert
    assert actual_answer == expected_answer


def test_subtract_twenty_takeaway_five_gives_fifteen():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 20
    number2 = 5
    expected_answer = 15

    # act
    actual_answer = calc.subtract(number1, number2)
    # assert
    assert actual_answer == expected_answer


def test_subtract_twenty_point_five_takeaway_five_point_zero_gives_fifteen_point_five():
    # triple A - AAA

    #   arrange
    calc = Calculator()
    number1 = 20.5
    number2 = 5.0
    expected_answer = 15.5

    # act
    actual_answer = calc.subtract(number1, number2)
    # assert
    assert actual_answer == expected_answer
