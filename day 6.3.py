# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.


def exponent(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result


base = 2
exp = 5
print(base, "raises to the power of ", exp, ":", exponent(base, exp))
