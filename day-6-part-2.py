# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 18:42:54 2025

@author: amanda
"""

import guard, tile

with open('Day6Input.txt') as file:
    instructions = file.read().split('\n')

result = 0
lab = []
obstructions = []
height = len(instructions)
width = len(instructions[0])
not_end = True

for x in range(height):
    lab.append([])
    for y in range(width):
        char = instructions[x][y]
        lab[x].append(tile.Tile(char))
        if x > 0:
            lab[x][y].connect_neigbour(lab[x - 1][y], 'N')
        if y > 0:
            lab[x][y].connect_neigbour(lab[x][y - 1], 'W')
        
        if char == '^':
            the_guard = guard.Guard(lab[x][y])

while not_end:
    not_end = the_guard.move_to_end()

the_guard.return_to_start()
the_guard.is_at.type = '.'
for x in range(height):
    for y in range(width):
        if lab[x][y].type == 'X':
            obstructions.append(lab[x][y])

for place in obstructions:
    not_end = True
    place.type = 'O'
    
    while not_end:
        not_end, in_loop = the_guard.move_to_loop()
        
        if in_loop:
            result += 1
            break
    
    place.type = '.'
    the_guard.return_to_start()

print(result)