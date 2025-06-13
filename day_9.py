# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:50:59 2025

@author: amanda
"""

with open('Day9Input.txt') as file:
    instructions = file.read()

disc_map_org = []

for i in range(len(instructions)):
    if i % 2:
        if not int(instructions[i]) == 0:
            disc_map_org.append([int(instructions[i])])
    else:
        disc_map_org.append([int(instructions[i]), int(i / 2)])

# --- Part 1 ---

result = 0
first_empty = -1
disc_map = [list(x) for x in disc_map_org]

while True:
    old_first_empty = first_empty
    for i in range(len(disc_map)):
        if len(disc_map[i]) == 1:
            first_empty = i
            break
    if old_first_empty == first_empty:
        break
    
    for i in range(len(disc_map) - 1, first_empty, -1):
        if len(disc_map[i]) > 1:
            last_full = i
            break
        else:
            disc_map.pop()
    
    if len(disc_map) - 1 == first_empty:
        disc_map.pop()
        break
    
    if disc_map[first_empty][0] == disc_map[last_full][0]:
        disc_map[first_empty].append(disc_map[last_full].pop())
    elif disc_map[first_empty][0] < disc_map[last_full][0]:
        disc_map[first_empty].append(disc_map[last_full][1])
        disc_map[last_full][0] -= disc_map[first_empty][0]
    else:
        disc_map[first_empty][0] -= disc_map[last_full][0]
        disc_map.insert(first_empty, disc_map.pop(last_full))

i = 0
while True:
    result += i * disc_map[0][1]
    disc_map[0][0] -= 1
    i += 1
    
    if disc_map[0][0] == 0:
        disc_map.pop(0)
    
    if not disc_map:
        break

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0
i = len(disc_map_org) - 1
data_to_move = disc_map_org[-1][1]
disc_map = [list(x) for x in disc_map_org]

while i > 0:
    if len(disc_map[i]) == 1:
        i -= 1
        continue
    if not disc_map[i][1] == data_to_move:
        i -= 1
        continue
    
    length = disc_map[i][0]
    
    for j in range(0, i):
        if len(disc_map[j]) == 1:
            if disc_map[j][0] == length:
                disc_map[j].append(disc_map[i].pop())
                break
            if disc_map[j][0] > length:
                disc_map[j][0] -= length
                disc_map.insert(j, [length, disc_map[i].pop()])
                i += 1
                break
    
    data_to_move -= 1
    i -= 1

while True:
    if disc_map[0][0] == 0:
        disc_map.pop(0)
    
        if not disc_map:
            break
        continue
    
    if len(disc_map[0]) == 2:
        result += i * disc_map[0][1]
    
    disc_map[0][0] -= 1
    i += 1

print(f'Part 2: {result}')