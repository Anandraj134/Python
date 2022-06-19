import random
import array

special_char = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}', '[', ']',
                ':', ':', '<', ',', '>', '.', '?', '/', '|']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']

UpperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

alpha = 1

length = 12

password = ''
COMBINED_LIST = numbers + UpperCase + LowerCase + special_char
rand_digit = random.choice(numbers)
rand_upper = random.choice(UpperCase)
rand_lower = random.choice(LowerCase)
rand_symbol = random.choice(special_char)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(length - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

for x in temp_pass_list:
    password = password + x

print(password)
