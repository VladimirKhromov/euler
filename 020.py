"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial_digit_sum(digit: int) -> int:
    if type(digit) != int or digit < 1:
        raise ValueError
    factorial_result = 1
    for i in range(2, digit + 1):
        factorial_result *= i

    result = sum([int(i) for i in str(factorial_result)])
    return result


try:
    assert factorial_digit_sum(2) == 2, "test 2"
    assert factorial_digit_sum(10) == 27, "test 10"
except AssertionError:
    print("test fail")



number = -1
print(f"The sum of the digits in the number {number}! is {factorial_digit_sum(number)}")