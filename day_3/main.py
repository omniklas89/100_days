print("Welcome to the rollercoaster!")
height = int(input("What is your height?"))
bill = 0

if height >= 120:
    age = int(input("Your age?"))
    if age <= 12:
        bill = 5
        print(f"OK, child ride and pay {bill}$")
    elif age <= 18:
        bill = 7
        print(f"You can ride and you pay {bill} for youth :))")
    elif 45 <= age <= 55:
        print("YOu ride for free!")
    else:
        bill = 12
        print(f"You can ride, but you pay {bill} bcs you are old!")
    
    picture = input("Wanna have a photo? y / n")
    if picture == "y":
        bill += 3
    print(f"You need to pay {bill}")
else:
    print("Sorry, neeed to eat more žganci! :D ")



# modulo % 10 % 5 0 (no remainder)

# number_to_check = int(input("Give me a number: "))
# print(f"number i am checking is {number_to_check}")

# if number_to_check % 2 == 0:
#     print("even")
# else:
#     print("Odd")
