# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")
j = 0
for i in range(10):
    sum = j + 1
    print("Current Number ", i, " Previous Number  ", j, "  Sum:", j + i)
    j = i
