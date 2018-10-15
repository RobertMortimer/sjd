#https://docs.python.org/3/library/functools.html
import functools

my_list = [1, 2, 3, 4, 5]

sum = functools.reduce(lambda x, y: x + y, my_list)

print(sum)