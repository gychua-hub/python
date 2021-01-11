import random

print("This is a dice simulator")
x = "y"

while x == "y":
    number = random.randint(1, 6)
    print("----------")

    if number == 1:
        print("|        |")
        print("|    O   |")
        print("|        |")
    if number == 2:
        print("|        |")
        print("| O    O |")
        print("|        |")
    if number == 3:
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
    if number == 4:
        print("| O    O |")
        print("|        |")
        print("| O    O |")
    if number == 5:
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
    if number == 6:
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")

    print("----------")
    x = input("Press y to roll again ")

