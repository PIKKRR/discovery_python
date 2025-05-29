#!/bin/python3

number = int(input('Enter a number: '))

if number > 25:
    print('Error')
else:
    while number < 25:
        number += 1
        print(f'Inside the loop, my variable is {number}')