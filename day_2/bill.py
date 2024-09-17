print("Welcome to the print calculator!")
total = float(input("What is total bill?")) #100
percent = int(input("How much you wanna tip: 10, 12 or 15?")) #12
people = int(input("Number of splits?")) #3
result = round((total + (total * (percent/100))) / people,5) #(100 + 100*(12/100) / 3)

print(f"Each of {people} need to pay {result} out of total {total} with {percent}% tip!")