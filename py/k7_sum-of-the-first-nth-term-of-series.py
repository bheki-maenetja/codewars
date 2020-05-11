from math import fsum

# Description:
# Task:
# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# Rules:
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

# Examples:
# SeriesSum(1) => 1 = "1.00"
# SeriesSum(2) => 1 + 1/4 = "1.25"
# SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
# NOTE: In PHP the function is called series_sum().

# SOLUTION
def series_sum(n):
    num_sum = fsum([1/num for num in range(1, n * 3, 3)])
    num_string = str(round(num_sum, 2))
    if len(num_string.split('.')[-1]) <= 1: num_string += '0'
    return num_string