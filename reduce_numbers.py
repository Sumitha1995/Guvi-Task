from functools import reduce  # reduce function is imported from functools

num = [1, 2, 3, 4]    # list of numbers

res = reduce(lambda a, b: a * b, num)   # reduce will take 2 values at a time and multiply it

print(res)