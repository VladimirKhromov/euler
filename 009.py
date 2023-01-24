"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplet(limit: int):
    a, b, c = 1, 1, 1

    for x in range(limit // 2 + 1):
        for y in range(x + 1, limit // 2 + 1):
            for z in range(y + 1, limit // 2 + 1):
                if x + y + z == limit and x ** 2 + y ** 2 == z ** 2:
                    return x, y, z, x * y * z
    return f'Pythagorean triplet with sum {limit} not found'


try:
    assert pythagorean_triplet(12) == (3, 4, 5, 60), "mistake 1"
    assert pythagorean_triplet(30) == (5, 12, 13, 780), "mistake 2"
except AssertionError as e:
    print(f"Test fail, {e}")
else:
    print("Test ok")

result = pythagorean_triplet(1000)
print("the product abc is", result[3])
