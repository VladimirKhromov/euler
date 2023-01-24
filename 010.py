"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def the_sum_of_the_primes(limit: int):
    lst = [i for i in range(0, limit + 1)]
    lst[1] = 0
    for i in range(2, limit // 2):
        for j in range(2 * i, limit + 1, i):
            lst[j] = 0

    return sum(lst)


try:
    assert the_sum_of_the_primes(10) == 17, "assert 10"
    assert the_sum_of_the_primes(11) == 28, "assert 11"
except AssertionError as e:
    print(f"Test fail {e}")
else:
    print("Test ok")

result = the_sum_of_the_primes(2 * 10 ** 6)
print('the sum of all the primes below two million is', result)
