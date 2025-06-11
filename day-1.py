# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 13:34:10 2025

@author: amanda
"""

with open('Day1Input.txt') as file:
    instructions = file.readlines()

list1 = []
list2 = []

for line in instructions:
    value1, value2 = line.split('   ')
    list1.append(int(value1))
    list2.append(int(value2))

list1.sort()
list2.sort()

# --- Part 1 ---

result = 0

for l1, l2 in zip(list1, list2):
    if l1 < l2:
        result += l2 - l1
    else:
        result += l1 - l2

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0

for i in list1:
    times = list2.count(i)
    result += i * times

print(f'Part 2: {result}')