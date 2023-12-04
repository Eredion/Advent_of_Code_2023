import os
PATH = "/workspaces/Advent_of_Code_2023/day_1/"

## Part 1
with open(PATH + "input.txt", 'r') as file:
    data = file.read().split('\n')

lines = [''.join(c for c in s if c.isdigit()) for s in data]

numbers = [f"{l[0]}{l[-1]}" for l in lines]

result = sum([int(n) for n in numbers])

print(result)

## Part 2

numbers = {"one": 1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}