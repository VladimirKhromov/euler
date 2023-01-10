"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
limit_min = 1
limit_max = 20

min_value = 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
print(min_value)

    while True:
        temp = limit
        temp /= 2
        for i in range(min, max):
            if temp%i != 0:
                is_continue = False
        limit = temp
    













def the_smallest_number(min, max):
    """ not_work """
    limit = 1
    for i in range(min, max):
        limit *= i

    is_continue = True
    while True:
        temp = limit
        temp /= 2
        for i in range(min, max):
            if temp%i != 0:
                is_continue = False
        limit = temp
    
    return limit

