# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

list = [10, 20, 30, 33, 44, 555, 100]

for i in list:
    if i % 5 == 0:
        print(i)
