from time import sleep
from datetime import datetime
import shutil
import os
from os import path, listdir, mkdir

print("Opening application...")
if path.exists("Backup"):
    for file_name in listdir("Backup"):
        old_path = os.path.join("Backup", file_name)
        shutil.move(old_path, file_name)
    print("Files restored from backup! 📥")
else:
    mkdir("Backup")


def cal_add():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sleep(3)
    addition = number1 + number2
    with open("result.txt", "a") as f:
        f.write(str(addition) + "\n")
    return addition


def cal_sub():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sleep(3)
    sub = number1 - number2
    with open("result.txt", "a") as f:
        f.write(str(sub) + "\n")
    return sub


def cal_mul():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sleep(3)
    multiplication = number1 * number2
    with open("result.txt", "a") as f:
        f.write(str(multiplication) + "\n")
    return multiplication


def cal_div():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sleep(3)
    division = number1 / number2
    with open("result.txt", "a") as f:
        f.write(str(division) + "\n")
    return division


def cal_mod():
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sleep(3)
    mod = number1 % number2
    with open("result.txt", "a") as f:
        f.write(str(mod) + "\n")
    return mod


while True:
    try:
        print("=" * 30)
        print("Welcome to the number calculator")
        print("=" * 30)
        print(datetime.today().strftime("%m/%d/%Y"))
        print(
            "1. Addition ➕\n2. Subtraction ➖\n3. Multiplication ✖️\n4. Division ➗\n5. Modulo 😶\n6. see History 📖📘\n7. Exit 🚫")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            result = cal_add()
            print("your answer is: ", result, "👨‍🔬")
        elif choice == 2:
            result = cal_sub()
            print("your Answer is:", result)
        elif choice == 3:
            result = cal_mul()
            print("your Answer is:", result)
        elif choice == 4:
            result = cal_div()
            print("your Answer is:", result)
        elif choice == 5:
            result = cal_mod()
            print("your Answer is:", result)
        elif choice == 6:
            if path.exists("result.txt"):
                with open("result.txt", "r") as f:
                    print(f.read())
            else:
                print("No history recorded yet!")

        elif choice == 7:
            break

    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("You can't divide by zero")

print("\nCleaning up workspace... 🧹")
for file_name in listdir("."):
    if file_name.endswith(".txt"):
        new_path = os.path.join("Backup", file_name)
        shutil.move(file_name, new_path)

print(datetime.today().strftime("%m/%d/%Y"))
print("All files safely stored in Backup folder. Goodbye! ❁´◡`❁")