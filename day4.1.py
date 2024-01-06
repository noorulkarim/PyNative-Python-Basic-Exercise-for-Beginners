# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.


def list_check(a):
    if a[0] == a[-1]:
        return True
    else:
        return False


a = [10, 20, 30, 10, 11]
print(list_check(a))
