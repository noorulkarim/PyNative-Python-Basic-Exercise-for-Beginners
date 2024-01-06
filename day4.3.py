# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

phrase = "Emma is good developer. Emma is a writer hello Emma".lower()
list_phrase = phrase.split(" ")
print(list_phrase)
count = 0
for i in list_phrase:
    if "emma" == i:
        count += 1

print("Emma appeared", count, " times")
