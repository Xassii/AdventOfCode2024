# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 12:30:47 2025

@author: amanda
"""

def find_operator(result, part, nummbers):
    if not nummbers:
        if part == result:
            return True
        return False
    
    for i in ['+', '*']:
        if i == '+':
            correct = find_operator(result, part + nummbers[0], nummbers[1:])
        elif i == '*':
            correct = find_operator(result, part * nummbers[0], nummbers[1:])
        
        if correct:
            return correct
    
    return correct

def with_concat(result, part, nummbers):
    if not nummbers:
        if part == result:
            return True
        return False
    
    for i in ['+', '*', '||']:
        if i == '+':
            correct = with_concat(result, part + nummbers[0], nummbers[1:])
        elif i == '*':
            correct = with_concat(result, part * nummbers[0], nummbers[1:])
        elif i == '||':
            new_part = int(str(part) + str(nummbers[0]))
            correct = with_concat(result, new_part, nummbers[1:])
        
        if correct:
            return correct
    
    return correct

with open('Day7Input.txt') as file:
    instructions = file.readlines()

test_value = []
nummbers = []

for row in instructions:
    value, num = row.split(': ')
    numbs = num.split(' ')
    test_value.append(int(value))
    nummbers.append([int(x) for x in numbs])

# --- Part 1 ---

result = 0

for value, numbs in zip(test_value, nummbers):
    correct = find_operator(value, 0, numbs)
    
    if correct:
        result += value

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0

for value, numbs in zip(test_value, nummbers):
    correct = with_concat(value, 0, numbs)
    
    if correct:
        result += value

print(f'Part 2: {result}')