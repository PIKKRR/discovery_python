#!/bin/python3

number = int(input('Enter a number\n'))

i = 1

while i <= 9:
    result = number * i
    print(f'{i} x {number} = {result}')
    i += 1