# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 15:17:53 2025

@author: amanda
"""

import re

def multyply_if_correct(instruction):
    if len(instruction) < 5:
        return 0
    
    split_instruction = instruction.split(')')
    if len(split_instruction) == 1:
        return 0
    
    instruction = split_instruction[0]
    first_char = instruction[0]
    if not first_char == '(':
        return 0
    
    instruction = instruction[1:]
    split_instruction = instruction.split(',')
    if not len(split_instruction) == 2:
        return 0
    
    pattern = '[0-9][0-9]?[0-9]?'
    first = re.fullmatch(pattern, split_instruction[0])
    second = re.fullmatch(pattern, split_instruction[1])
    if first == None or second == None:
        return 0
    
    return int(split_instruction[0]) * int(split_instruction[1])

with open('Day3Input.txt') as file:
    instructions = file.read()

# --- Part 1 ---

result = 0

mul_instructions = instructions.split('mul')
mul_instructions.pop(0)

for instruction in mul_instructions:
    result += multyply_if_correct(instruction)

print(f'Part 1: {result}')

# --- Part 2 ---

new_instructions = []
mul_instructions = []
result = 0

do_instructions = instructions.split('do()')
for instruction in do_instructions:
    do_first_instruction = instruction.split("don't()")
    new_instructions.append(do_first_instruction[0])

for instruction in new_instructions:
    mul_parts = instruction.split('mul')
    mul_parts.pop(0)
    
    mul_instructions = mul_instructions + mul_parts

for instruction in mul_instructions:
    result += multyply_if_correct(instruction)

print(f'Part 2: {result}')