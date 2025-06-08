# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 13:34:10 2025

@author: amanda
"""

list1 = []
list2 = []
result = 0

with open('Day1Input.txt') as file:
    instructions = file.readlines()

for line in instructions:
    value1, value2 = line.split('   ')
    list1.append(int(value1))
    list2.append(int(value2))

list1.sort()
list2.sort()

# --- Part 1 ---

for i in range(len(list1)):
    if list1[i] < list2[i]:
        result += list2[i] - list1[i]
    else:
        result += list1[i] - list2[i]

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0

for i in list1:
    times = list2.count(i)
    result += i * times

print(f'Part 2: {result}')