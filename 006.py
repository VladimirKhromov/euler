"""
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squares(i: int) -> int:
    """ The sum of the squares of the first i natural numbers. """
    res = 0
    for i in range(1, i + 1):
        res += i ** 2
    return res


def square_of_the_sum(i: int) -> int:
    """ The square of the sum of the first ten natural numbers. """
    return sum(range(1, i + 1)) ** 2


try:
    number = 10
    assert square_of_the_sum(number) - sum_of_squares(number) == 2640
except AssertionError:
    print("Test fail")
else:
    print("Test ok")

number = 100
result = square_of_the_sum(number) - sum_of_squares(number)
print(f"The difference between the sum of the squares of "
      f"the first {number} natural numbers and the square of the sum is {result}")
