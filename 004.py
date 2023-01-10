"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def palindrome():
    large_number = 0
    coord = None
    for i in range(999, 100, -1):
        for j in range (i, 100, -1):
            res = i * j
            if str(res) == str(res)[::-1]:
                large_number = max(large_number, res)
                if res == large_number:
                    coord = (i, j)
    print(large_number, coord)
    return large_number

palindrome()