"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def divisors(number: int) -> list[int]:
    if type(number) != int and number < 2:
        raise ValueError
    result = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result.append(i)
    return result


def amicable_numbers(number: int):
    guess = sum(divisors(number))
    if sum(divisors(guess)) == number and guess != number:
        return True, (number, guess)
    else:
        return False, (number, guess)


def sum_of_all_the_amicable_numbers(limit: int) -> int:
    good_result_list = []
    bad_result_list = []
    for i in range(3, limit + 1):
        if (i not in good_result_list) and (i not in bad_result_list):
            amicable = amicable_numbers(i)
            if amicable[0]:
                good_result_list.append(amicable[1][0])
                good_result_list.append(amicable[1][1])
            else:
                bad_result_list.append(amicable[1][0])
                bad_result_list.append(amicable[1][1])
    return sum(good_result_list)


# some test
"""
try:
    assert divisors(1) == [1], "divisors(1)"
    assert divisors(2) == [1], "divisors(2)"
    assert divisors(220) == [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110], "divisors(220)"
    assert divisors(284) == [1, 2, 4, 71, 142], "divisors(284)"
    assert amicable_numbers(220) == (True, (220, 284)), "amicable_numbers(220)"
    assert amicable_numbers(284) == (True, (284, 220)), "amicable_numbers(284)"
    assert amicable_numbers(5) == (False, (5, 1)), "amicable_numbers(5)"
    assert amicable_numbers(10) == (False, (10, 8)), "amicable_numbers(10)"
    assert sum_of_all_the_amicable_numbers(1) == 0, "sum_of_all_the_amicable_numbers(1)"
    assert sum_of_all_the_amicable_numbers(284) == 504, "sum_of_all_the_amicable_numbers(284)"
except AssertionError as e:
    print(f"test {e} fail")
"""

number = 10 ** 4
result = sum_of_all_the_amicable_numbers(number)
print(f"The sum of all the amicable numbers under {number} is {result}")
