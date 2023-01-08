"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.

"""

limit = 4 * 10**6
i1, i2 = 1, 2
result = 0
while i2 < limit:
    if i2 % 2 == 0:
        result += i2
    i1, i2 = i2, i1 + i2

print(f'Sum of the even-valued terms in the Fibonacci sequence(not exceed {limit}): {result}')