import string
import random

# for loops !

# fruts = ["apple","peach","pear"]
# for fruit in fruts:
#     print(fruit)
#     print(fruit + " and this!")

# student_scores = [123,333,117,200,67,23,55,98,100,11,76,56,62,24]

# total = sum(student_scores)
# print(total)

# sum = 0
# for score in student_scores:
#     sum += score

# print(sum)

# student_scores = [123,333,117,200,67,23,55,98,100,11,76,56,62,24]

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(f"Max score is {max_score}")

# sum = 0
# for numbers in range(1,101):
#     sum += numbers

# print(f"Sum of range 1 - 101 is = {sum}")


## Project Password Generator

letters = ["a","b","c","d","e","g","i","j","k","l","m","y","x","o","p"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbols = ["_","!","#","?","$","%"]

number_of_letters = int(input("Home many letters?\n"))
number_of_numbers = int(input("Home many numbers?\n"))
number_of_symbols = int(input("Home many symbols?\n"))

final_password = []

for letter in range(0, number_of_letters):
    final_password += random.choice(letters)
for number in range(0, number_of_numbers):
    final_password += random.choice(numbers)
for symbol in range(0, number_of_symbols):
    final_password += random.choice(symbols)

random.shuffle(final_password)

password = ""
for char in final_password:
    password += char

print(f"Your final password is:{password}")