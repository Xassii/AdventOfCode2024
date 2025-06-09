# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 16:30:06 2025

@author: amanda
"""

with open('Day6Input.txt') as file:
    instructions = file.read().split('\n')

result = 0
guard_at = []
guard_facing = 'N'
height = len(instructions)
width = len(instructions[0])

for x, line in enumerate(instructions):
    if '^' in line:
        guard_at.append(x)
        for y, char in enumerate(line):
            if char == '^':
                guard_at.append(y)
                break
        break

for x in range(height):
    instructions[x] = list(instructions[x])

while True:
    leave_n = guard_at[0] == 0 and guard_facing == 'N'
    leave_s = guard_at[0] == height - 1 and guard_facing == 'S'
    leave_w = guard_at[1] == 0 and guard_facing == 'W'
    leave_e = guard_at[1] == width - 1 and guard_facing == 'E'
    if leave_n or leave_s or leave_e or leave_w:
        instructions[guard_at[0]][guard_at[1]] = 'X'
        break
    
    if guard_facing == 'N':
        if instructions[guard_at[0] - 1][guard_at[1]] == '#':
            guard_facing = 'E'
        else:
            instructions[guard_at[0]][guard_at[1]] = 'X'
            guard_at[0] -= 1
    elif guard_facing == 'S':
        if instructions[guard_at[0] + 1][guard_at[1]] == '#':
            guard_facing = 'W'
        else:
            instructions[guard_at[0]][guard_at[1]] = 'X'
            guard_at[0] += 1
    elif guard_facing == 'W':
        if instructions[guard_at[0]][guard_at[1] - 1] == '#':
            guard_facing = 'N'
        else:
            instructions[guard_at[0]][guard_at[1]] = 'X'
            guard_at[1] -= 1
    else:
        if instructions[guard_at[0]][guard_at[1] + 1] == '#':
            guard_facing = 'S'
        else:
            instructions[guard_at[0]][guard_at[1]] = 'X'
            guard_at[1] += 1

for line in instructions:
    result += ''.join(line).count('X')

print(result)