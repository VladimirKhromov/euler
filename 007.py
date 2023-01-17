"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
from math import sqrt


def is_prime(number: int) -> bool:
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def prime_number(number: int) -> int:
    # if number in range(3):
    #     return [1, 2, 3][number]
    # if number < 0:
    #     raise ValueError
    count = 2
    value = 3
    end_count = number
    while count < end_count:
        value += 2
        if is_prime(value):
            count += 1
    return value


print(prime_number(10001))
