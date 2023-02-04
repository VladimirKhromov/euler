"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def long_fibonacci(long: int) -> int:
    if type(long) != int and long < 2:
        raise ValueError
    fib, l_fib = 1, 1  # first and second Fibonacci
    index = 2
    while len(str(fib)) < long:
        fib, l_fib = fib + l_fib, fib
        index += 1
    return index


try:
    assert long_fibonacci(2) == 7, "long_fibonacci(2)"
    assert long_fibonacci(3) == 12, "long_fibonacci(3)"
except AssertionError as e:
    print(f"test {e} fail")

lon = 1000
result = long_fibonacci(lon)
print(f"Index of the first term in the Fibonacci sequence to contain {lon} digits is {result}")
