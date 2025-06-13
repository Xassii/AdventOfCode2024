# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 11:17:28 2025

@author: amanda
"""

import tile, collections

with open('Day12Input.txt') as file:
    instructions = file.read().split('\n')

garden = []
patch_id = 1
patch_size = {}

for x, line in enumerate(instructions):
    garden.append([])
    for y, plant in enumerate(line):
        garden[x].append(tile.GardenPlot(plant))
        
        if x > 0:
            garden[x][y].connect_neigbour(garden[x - 1][y], 'N')
        if y > 0:
            garden[x][y].connect_neigbour(garden[x][y - 1], 'W')

for row in garden:
    for plot in row:
        if not plot.id:
            size = plot.explore_patch(patch_id)
            patch_size[patch_id] = size
            patch_id += 1

# --- Part 1 ---

result = 0
tracking = garden[0][0].tracker

# for row in garden:
#     for plot in row:
#         if not plot.explored:
#             size, fences = plot.explore_patch()
#             result += size * fences

for row in garden:
    for plot in row:
        if tracking == plot.tracker:
            fences = plot.count_fences()
            result += fences * patch_size[plot.id]

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0
fences = collections.defaultdict(int)

for plot in garden[0]:
    new_fences = plot.count_region_sides('S', ('E', 'W'), [], '')
    for plot_id, num in new_fences.items():
        fences[plot_id] += num

for plot in [x[0] for x in garden]:
    new_fences = plot.count_region_sides('E', ('N', 'S'), [], '')
    for plot_id, num in new_fences.items():
        fences[plot_id] += num

for plot_id, size in patch_size.items():
    result += fences[plot_id] * size

print(f'Part 2: {result}')