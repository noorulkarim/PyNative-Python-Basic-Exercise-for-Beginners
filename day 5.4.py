# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

num='7536'
rev_num=num[::-1]

for i in rev_num:
    print(i, end=" ")