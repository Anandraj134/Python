# Given a string as input, you need to output how many times each letter appears in the string. You decide to store
# the data in a dictionary, with the letters as the keys, and the corresponding counts as the values. Create a
# program to take a string as input and output a dictionary, which represents the letter count.

text = input()
dict1 = {}

for i in text:
    count = text.count(i)
    dict1[i] = count

print(dict1)
