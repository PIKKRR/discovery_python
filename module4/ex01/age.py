#!/bin/python3

while True:
    try:
        age = int(input("Please tell me your age: "))
        if age > 0:
            break
        else:
            print("Error, age must be a positive integer.")
    except ValueError:
        print("Error, please enter a valid number.")

print(f"In 10 years, you'll be {age + 10} years old.")
print(f"In 20 years, you'll be {age + 20} years old.")
print(f"In 30 years, you'll be {age + 30} years old.")