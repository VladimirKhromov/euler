"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

"""

# TO DO late!

limit = 600851475143

def nod(n:int) -> list:
    if n >= 50000:
        print('very large number')
        raise ValueError("very large number")

    result = []
    for i in range(n-1, 1, -1):
        if n % i == 0:
            if not nod(i):
                result.append(i)
    result.sort()
    return result

try:
    assert nod(13195) == [5, 7, 13, 29]
except AssertionError:
    print("Test error")
else:
    print('Test OK')

print(nod(600851475143))