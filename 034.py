"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import prod


def factorial(number: int) -> int:
    return prod(range(1, number + 1))


assert factorial(5) == 120, "fac5"
assert factorial(4) == 24, "fac4"
assert factorial(1) == 1, "fac1"
assert factorial(2) == 2, "fac2"


def is_sum_fac(number: int) -> bool:
    str_num = list(map(int, str(number)))
    return number == sum([factorial(i) for i in str_num])


result = [i for i in range(3, 10 ** 6) if is_sum_fac(i)]

print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is {sum(result)}")
