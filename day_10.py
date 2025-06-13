# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 18:19:10 2025

@author: amanda
"""

import directionles_tile as tile

with open('Day10Input.txt') as file:
    instructions = file.read().split('\n')

the_map = []
result1 = 0
result2 = 0

for x, line in enumerate(instructions):
    the_map.append([])
    for y, num in enumerate(line):
        if num == '0':
            the_map[x].append(tile.HikingTile(int(num), x, y))
        else:
            the_map[x].append(tile.HikingTile(int(num)))
        
        current = the_map[x][y]
        if x > 0:
            current.connect_tile(the_map[x - 1][y])
        if y > 0:
            current.connect_tile(the_map[x][y - 1])

for line in the_map:
    for part in line:
        if part.height == 0:
            part.find_summit()

for line in the_map:
    for part in line:
        if part.height == 9:
            trails = part.connected_trailheads
            result1 += len(set(trails))
            result2 += len(trails)

print(f'Part 1: {result1}')
print(f'Part 2: {result2}')