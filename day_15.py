# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 17:42:25 2025

@author: amanda
"""

import tile, gps_robot

with open('Day15Input.txt') as file:
    instructions = file.read().split('\n')

for i in range(len(instructions)):
    if not instructions[i]:
        warehouse_string = instructions[:i]
        instructions = ''.join(instructions[i + 1:])
        break

directions = ''
for instruction in instructions:
    if instruction == '<':
        directions += 'W'
    elif instruction == '>':
        directions += 'E'
    elif instruction == '^':
        directions += 'N'
    else:
        directions += 'S'

# --- Part 1 ---

result = 0
warehouse = []

for y, row in enumerate(warehouse_string):
    warehouse.append([])
    for x, t in enumerate(row):
        if t == '@':
            warehouse[y].append(tile.Tile('@'))
            robot_start = warehouse[y][x]
        else:
            warehouse[y].append(tile.Tile(t))
        
        if y > 0:
            warehouse[y][x].connect_neigbour(warehouse[y - 1][x], 'N')
        if x > 0:
            warehouse[y][x].connect_neigbour(warehouse[y][x - 1], 'W')

height = len(warehouse)
width = len(warehouse[0])
the_robot = gps_robot.GPSRobot(robot_start)

for direction in directions:
    the_robot.move(direction)

for y in range(1, height):
    for x in range(1, width):
        if warehouse[y][x].type == 'O':
            result += (100 * y) + x

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0
warehouse = []

for y, row in enumerate(warehouse_string):
    warehouse.append([])
    for x, t in enumerate(row):
        if t == '@':
            warehouse[y].append(tile.Tile('@'))
            warehouse[y].append(tile.Tile('.'))
            robot_start = warehouse[y][x * 2]
        elif t == 'O':
            warehouse[y].append(tile.Tile('['))
            warehouse[y].append(tile.Tile(']'))
        else:
            warehouse[y].append(tile.Tile(t))
            warehouse[y].append(tile.Tile(t))
        
        one = warehouse[y][x * 2]
        two = warehouse[y][x * 2 + 1]
        
        two.connect_neigbour(one, 'W')
        if y > 0:
            one.connect_neigbour(warehouse[y - 1][x * 2], 'N')
            two.connect_neigbour(warehouse[y - 1][x * 2 + 1], 'N')
        if x > 0:
            one.connect_neigbour(warehouse[y][x * 2 - 1], 'W')

height = len(warehouse)
width = len(warehouse[0])
the_robot = gps_robot.GPSRobot(robot_start)

for direction in directions:
    the_robot.wide_move(direction)

for y in range(1, height):
    for x in range(2, width):
        if warehouse[y][x].type == '[':
            result += (100 * y) + x

print(f'Part 2: {result}')