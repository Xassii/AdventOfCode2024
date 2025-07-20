# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 08:27:33 2025

@author: amanda
"""

import tile


def get_opposit_direction(direction):
    if direction == 'N':
        return 'S'
    if direction == 'E':
        return 'W'
    if direction == 'S':
        return 'N'
    return 'E'


def sort_directions(old_list):
    new_list = []
    
    if 'E' in old_list:
        new_list.append('E')
    if 'S' in old_list:
        new_list.append('S')
    if 'W' in old_list:
        new_list.append('W')
    if 'N' in old_list:
        new_list.append('N')
    
    return new_list


def find_shortest_path(is_at, been_at, direc, dist, max_dist):
    if is_at.type:
        return min(dist, max_dist)
    if dist >= max_dist:
        return max_dist
    
    directions = list(is_at.neigbour.keys())
    directions.remove(get_opposit_direction(direc))
    directions = sort_directions(directions)
    
    been_at.append(is_at.position)
    
    for direction in directions:
        go_to = is_at.neigbour[direction]
        if go_to == None:
            continue
        
        shorter = is_at.remember[direction] > dist
        not_been = not go_to.position in been_at
        if shorter and not_been:
            is_at.remember[direction] = dist
            values = (go_to, been_at, direction, dist + 1, max_dist)
            max_dist = find_shortest_path(*values)
    
    been_at.pop()
    
    return max_dist


def find_exit(is_at, been_at, direc):# TODO
    if is_at.type:
        return True
    
    directions = list(is_at.neigbour.keys())
    if direc:
        directions.remove(get_opposit_direction(direc))
    
    been_at.append(is_at.position)
    
    for direction in directions:
        go_to = is_at.neigbour[direction]
        if go_to == None:
            continue
        if go_to.position == None:
            continue
        
        if not go_to.position in been_at:
            result = find_exit(go_to, been_at, direction)
            if result:
                return result
    
    been_at.pop()
    
    return False


with open('Day18Input.txt') as file:
    instructions = file.readlines()

instruction1 = instructions[:1024]
instruction2 = instructions[1024:]
memory_space = []

for y in range(71):
    memory_space.append([])
    for x in range(71):
        memory_space[y].append(tile.Tile(False, (x, y)))
        
        if y > 0:
            memory_space[y][x].connect_neigbour(memory_space[y - 1][x], 'N')
            memory_space[y][x].remember['N'] = 71*71
            memory_space[y - 1][x].remember['S'] = 71*71
        if x > 0:
            memory_space[y][x].connect_neigbour(memory_space[y][x - 1], 'W')
            memory_space[y][x].remember['W'] = 71*71
            memory_space[y][x - 1].remember['E'] = 71*71

for i in instruction1:
    instruction = i.split(',')
    x = int(instruction[0])
    y = int(instruction[1])
    
    memory_space[y][x].disconnect_neigbours()
    memory_space[y][x] = None

memory_space[70][70].type = True

# --- Part 1 ---

memory_space[0][0].remember['E'] = 0
memory_space[0][0].remember['S'] = 0
result = find_shortest_path(memory_space[0][1], [], 'E', 1, 71*71)
result = find_shortest_path(memory_space[1][0], [], 'S', 1, result)

print(f'Part 1: {result}')

# --- Part 2 ---

for i in instruction2:
    instruction = i.split(',')
    x = int(instruction[0])
    y = int(instruction[1])
    
    memory_space[y][x].position = None

instruction2.reverse()

for i in instruction2:
    instruction = i.split(',')
    x = int(instruction[0])
    y = int(instruction[1])
    
    memory_space[y][x].position = (x, y)
    
    found_exit = find_exit(memory_space[0][0], [], '')
    
    if found_exit:
        print(f'Part 2: {x},{y}')
        break