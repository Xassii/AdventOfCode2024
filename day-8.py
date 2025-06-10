# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 13:21:47 2025

@author: amanda
"""

from collections import defaultdict


def calculate_antinodes(coords):
    antinode = []
    while True:
        the_tower = coords.pop(0)
        if not coords:
            return antinode
        
        for tower in coords:
            if the_tower[0] < tower[0] and the_tower[1] < tower[1]:
                dist_x = tower[0] - the_tower[0]
                dist_y = tower[1] - the_tower[1]
                antinode.append((the_tower[0] - dist_x, the_tower[1] - dist_y))
                antinode.append((tower[0] + dist_x, tower[1] + dist_y))
                
            elif the_tower[0] > tower[0] and the_tower[1] < tower[1]:
                dist_x = the_tower[0] - tower[0]
                dist_y = tower[1] - the_tower[1]
                antinode.append((the_tower[0] + dist_x, the_tower[1] - dist_y))
                antinode.append((tower[0] - dist_x, tower[1] + dist_y))
                
            elif the_tower[0] < tower[0] and  the_tower[1] > tower[1]:
                dist_x = tower[0] - the_tower[0]
                dist_y = the_tower[1] - tower[1]
                antinode.append((the_tower[0] - dist_x, the_tower[1] + dist_y))
                antinode.append((tower[0] + dist_x, tower[1] - dist_y))
                
            elif the_tower[0] > tower[0] and  the_tower[1] > tower[1]:
                dist_x = the_tower[0] - tower[0]
                dist_y = the_tower[1] - tower[1]
                antinode.append((the_tower[0] + dist_x, the_tower[1] + dist_y))
                antinode.append((tower[0] - dist_x, tower[1] - dist_y))


def get_coords(tower1, tower2, height, width):
    antinode = []
    dist_x = abs(tower1[0] - tower2[0])
    dist_y = abs(tower1[1] - tower2[1])
    x1 = tower1[0]
    y1 = tower1[1]
    x2 = tower2[0]
    y2 = tower2[1]
    
    if x1 < x2 and y1 < y2:
        while x1 >= 0 and y1 >= 0:
            antinode.append((x1, y1))
            x1 -= dist_x
            y1 -= dist_y
        while x2 < height and y2 < width:
            antinode.append((x2, y2))
            x2 += dist_x
            y2 += dist_y
    elif x1 > x2 and y1 < y2:
        while x1 < height and y1 >= 0:
            antinode.append((x1, y1))
            x1 += dist_x
            y1 -= dist_y
        while x2 >= 0 and y2 < width:
            antinode.append((x2, y2))
            x2 -= dist_x
            y2 += dist_y
    elif x1 < x2 and y1 > y2:
        while x1 >= 0 and y1 < width:
            antinode.append((x1, y1))
            x1 -= dist_x
            y1 += dist_y
        while x2 < height and y2 >= 0:
            antinode.append((x2, y2))
            x2 += dist_x
            y2 -= dist_y
    elif x1 > x2 and y1 > y2:
        while x1 < height and y1 < width:
            antinode.append((x1, y1))
            x1 += dist_x
            y1 += dist_y
        while x2 >= 0 and y2 >= 0:
            antinode.append((x2, y2))
            x2 -= dist_x
            y2 -= dist_y
    
    return antinode


def calculate_all_antinodes(coords, height, width):
    antinode = []
    while True:
        the_tower = coords.pop(0)
        antinode.append((the_tower[0], the_tower[1]))
        if not coords:
            return antinode
        
        for tower in coords:
            antinode += get_coords(the_tower, tower, height, width)


with open('Day8Input.txt') as file:
    instructions = file.read().split('\n')

height = len(instructions)
width = len(instructions[0])
antennas = defaultdict(list)

for x, row in enumerate(instructions):
    for y, char in enumerate(row):
        if not char == '.':
            antennas[char].append([x, y])

# --- Part 1 ---

result = 0
antinodes = []

for key in antennas.keys():
    antinodes += calculate_antinodes(list(antennas[key]))

antinodes = list(set(antinodes))
for node in antinodes:
    in_x = node[0] >= 0 and node[0] < height
    in_y = node[1] >= 0 and node[1] < width
    if in_x and in_y:
        result += 1

print(f'Part 1: {result}')

# --- Part 2 ---

antinodes = []

for key in antennas.keys():
    if len(antennas[key]) > 1:
        antinodes += calculate_all_antinodes(antennas[key], height, width)

antinodes = list(set(antinodes))
result = len(antinodes)

print(f'Part 2: {result}')