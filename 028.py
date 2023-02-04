"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def spiral_diagonals(size: int) -> int:
    limit = (size - 1) // 2
    summary = 1
    number = 1
    circle = 1
    while circle <= limit:
        sum_number = [number + 2 * circle,
                      number + 4 * circle,
                      number + 6 * circle,
                      number + 8 * circle,
                      ]
        summary += sum(sum_number)
        number = sum_number[-1]
        circle += 1
    return summary


try:
    assert spiral_diagonals(5) == 101, "spiral_diagonals(5)"
    assert spiral_diagonals(7) == 261, "spiral_diagonals(7)"
except AssertionError as e:
    print(f"test {e} fail")

spiral = 1001
result = spiral_diagonals(spiral)
print(f"The sum of the numbers on the diagonals in a {spiral} by {spiral} spiral is {result}")
