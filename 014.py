"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(num: int, chain=0):
    if num == 1:
        return chain + 1
    elif num % 2 == 0:
        num = num // 2
        chain = collatz(num, chain + 1)
    else:
        num = 3 * num + 1
        chain = collatz(num, chain + 1)
    return chain


assert collatz(2) == 2, "collatz(2)"
assert collatz(13) == 10, "collatz(13)"
assert collatz(8) == 4, "collatz(8)"
# assert collatz(837799) == 525, "collatz(837799)"


maximum = [1, 1]
for i in range(499999, 10 ** 6, 2):
    result = collatz(i)
    if result > maximum[0]:
        maximum = [result, i]
print(f"The longest chain for {maximum[1]} is {maximum[0]}")
