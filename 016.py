"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


def sum_of_the_digits_degree_of_2(degree: int) -> int:
    number = 2 ** degree
    return sum([int(i) for i in str(number)])


assert sum_of_the_digits_degree_of_2(15) == 26

print(sum_of_the_digits_degree_of_2(1000))
