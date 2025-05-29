#!/bin/python3

while True:
    try:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid integers only.")
        continue

    print(f'{n1} + {n2} = {n1 + n2}')
    print(f'{n1} - {n2} = {n1 - n2}')
    if n2 == 0:
        print(f'{n1} / {n2} = You can\'t divide by zero!')
    else:
        print(f'{n1} / {n2} = {int(n1 / n2)}')
    print(f'{n1} * {n2} = {n1 * n2}')

    break