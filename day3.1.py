# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.


def remove_chars(str, num):
    new_word = ""
    for i in range(num, len(str)):
        new_word += str[i]
    return new_word


print(remove_chars("pynative", 2))