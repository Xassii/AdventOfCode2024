# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 09:43:16 2025

@author: amanda
"""

import math
from collections import defaultdict

def check_order(uppdate, rules, length):
    for i in range(length - 1):
        for j in range(i + 1, length):
            if uppdate[i] in rules[uppdate[j]]:
                return False
    return True

def rule_sort(unsorted, rules, length):
    while True:
        is_sorted = True
        for i in range(length - 1):
            if unsorted[i] in rules[unsorted[i + 1]]:
                temp = unsorted[i]
                unsorted[i] = unsorted[i + 1]
                unsorted[i + 1] = temp
                is_sorted = False
        
        if is_sorted:
            return unsorted

rules = defaultdict(list)
uppdates = []
not_correct = []

with open('Day5Input.txt') as file:
    instructions = file.readlines()

for line in instructions:
    if '|' in line:
        first, second = line.split('|')
        rules[int(first)].append(int(second))
    if ',' in line:
        uppdates.append([int(x) for x in line.split(',')])

# --- Part 1 ---

result = 0

for uppdate in uppdates:
    length = len(uppdate)
    correct = check_order(uppdate, rules, length)
    
    if correct:
        middle = math.floor(length / 2)
        result += uppdate[middle]
    else: # For part 2
        not_correct.append(uppdate)

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0

for uppdate in not_correct:
    length = len(uppdate)
    rule_sort(uppdate, rules, length)
    middle = math.floor(length / 2)
    result += uppdate[middle]

print(f'Part 2: {result}')