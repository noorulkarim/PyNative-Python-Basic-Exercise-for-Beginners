# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

str='127'
rev_str=str[::-1]

print ("Original Number:",str)
if(str[0]==rev_str[0]):
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")