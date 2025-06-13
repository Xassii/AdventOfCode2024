# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 09:26:55 2025

@author: amanda
"""

import time, tile, robot

with open('Day14Input.txt') as file:
    instructions = file.readlines()

floor = []
positions = []
velocities = []

for line in instructions:
    p, v = line.split(' v=')
    p = p[2:].split(',')
    v = v.split(',')
    
    positions.append([int(x) for x in p])
    velocities.append([int(x) for x in v])

# --- Part 1 ---

quadrant1 = 0
quadrant2 = 0
quadrant3 = 0
quadrant4 = 0

full_dist = [[x * 100, y * 100] for x, y in velocities]
end_pos = [[a[0] + b[0], a[1] + b[1]] for a, b in zip(positions, full_dist)]
end_pos = [[x % 101, y % 103] for x, y in end_pos]

for pos in end_pos:
    if pos[0] < 50 and pos[1] < 51:
        quadrant1 += 1
    elif pos[0] > 50 and pos[1] < 51:
        quadrant2 += 1
    elif pos[0] < 50 and pos[1] > 51:
        quadrant3 += 1
    elif pos[0] > 50 and pos[1] > 51:
        quadrant4 += 1

print(f'Part 1: {quadrant1 * quadrant2 * quadrant3 * quadrant4}')

# --- Part 2 ---

floor = []
robots = []

for y in range(103):
    floor.append([])
    for x in range(101):
        floor[y].append(tile.Tile(0))
        if y > 0:
            floor[y][x].connect_neigbour(floor[y - 1][x], 'N')
        if x > 0:
            floor[y][x].connect_neigbour(floor[y][x - 1], 'W')

for i in range(101):
    floor[0][i].connect_neigbour(floor[-1][i], 'N')
for i in floor:
    i[0].connect_neigbour(i[-1], 'W')

for bot in zip(positions, velocities):
    place = floor[bot[0][1]][bot[0][0]]
    robots.append(robot.Robot(place, bot[1]))
    place.type += 1

i = 0
while True:
    if not (15 + i) % 103 and not (89 + i) % 101:
        #time.sleep(0.25)
        print(f'\n\n{"O"*40}-----  {i}  -----{"O"*40}\n')
        for y in floor:
            temp = ''
            for x in y:
                if x.type == 0:
                    temp += ' '
                else:
                    temp += 'O'
            print(temp)
        break
    i += 1
    
    for bot in robots:
        bot.move()
    #time.sleep(0.25)

# Horisontal every 103: 88 191...
# Vertical every 101:   12 113...