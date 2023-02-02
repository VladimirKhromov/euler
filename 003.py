"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""


def prime_factors(number: int) -> int:
    count = 2
    while True:
        if number % count == 0:
            number /= count
            if number == 1:
                return count
        count += 1


try:
    assert prime_factors(13195) == 29
except AssertionError:
    print("prime_factors fail")

number = 600851475143
result = prime_factors(number)
print(f"The largest prime factor of the {number} is {result}")
