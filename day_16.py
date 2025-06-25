# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 19:17:43 2025

@author: amanda
"""

import tile


def determine_opposite(d):
    if d == 'N':
        return 'S'
    elif d == 'E':
        return 'W'
    elif d == 'S':
        return 'N'
    else:
        return 'E'


def find_shortest(is_at, facing, score, been_at, min_score):
    opposite = determine_opposite(facing)
    
    while True:
        if is_at.type == 'E':
            return min(score, min_score)
        if score > min_score:
            return min_score
        if len(is_at.neigbour) == 1:
            return min_score
        if len(is_at.neigbour) > 2 and is_at.position in been_at:
            return min_score
        
        directions = list(is_at.neigbour.keys())
        directions.remove(opposite)
        if len(is_at.neigbour) > 2:
            been_at.append(is_at.position)
            break
        
        if directions[0] == facing:
            score += 1
        else:
            score += 1001
            facing = directions[0]
            opposite = determine_opposite(facing)
        is_at = is_at.neigbour[directions[0]]
    
    for direction in directions:
        going_to = is_at.neigbour[direction]
        
        new_score = score + 1
        if not direction == facing:
            new_score += 1000
        
        if is_at.remember[direction] <= new_score:
            continue
        else:
            is_at.remember[direction] = new_score
        
        values = (going_to, direction, new_score, been_at, min_score)
        min_score = find_shortest(*values)
    
    been_at.remove(is_at.position)
    
    return min_score


def find_paths(is_at, facing, score, been_at, max_score):
    opposite = determine_opposite(facing)
    path = set()
    result_path = set()
    
    while True:
        path.add(is_at.position)
        
        if is_at.type == 'E':
            return path
        if score > max_score:
            return set()
        if len(is_at.neigbour) == 1:
            return set()
        if len(is_at.neigbour) > 2 and is_at.position in been_at:
            return set()
        
        directions = list(is_at.neigbour.keys())
        directions.remove(opposite)
        if len(is_at.neigbour) > 2:
            been_at.append(is_at.position)
            break
        
        if directions[0] == facing:
            score += 1
        else:
            score += 1001
            facing = directions[0]
            opposite = determine_opposite(facing)
        is_at = is_at.neigbour[directions[0]]
    
    for direction in directions:
        going_to = is_at.neigbour[direction]
        
        new_score = score + 1
        if not direction == facing:
            new_score += 1000
        
        if is_at.remember[direction] < new_score:
            continue
        else:
            is_at.remember[direction] = new_score
        
        values = (going_to, direction, new_score, been_at, max_score)
        result = find_paths(*values)
        result_path.update(result)
    
    been_at.remove(is_at.position)
    if result_path:
        result_path.update(path)
    
    return result_path


with open('Day16Input.txt') as file:
    instructions = file.readlines()

maze = []

for y, line in enumerate(instructions):
    maze.append([])
    for x, char in enumerate(line):
        maze[y].append(tile.Tile(char, (x, y)))
        if char == 'S':
            start = maze[y][x]
        
        if x > 0:
            one = maze[y][x].type in ('.', 'S', 'E')
            two = maze[y][x - 1].type in ('.', 'S', 'E')
            if one and two:
                maze[y][x].connect_neigbour(maze[y][x - 1], 'W')
                maze[y][x].remember['W'] = 1000000
                maze[y][x - 1].remember['E'] = 1000000
        if y > 0:
            one = maze[y][x].type in ('.', 'S', 'E')
            two = maze[y - 1][x].type in ('.', 'S', 'E')
            if one and two:
                maze[y][x].connect_neigbour(maze[y - 1][x], 'N')
                maze[y][x].remember['N'] = 1000000
                maze[y - 1][x].remember['S'] = 1000000

# --- Part 1 ---

been_at = [start.position]
min_score = 1000000

for direction, n in start.neigbour.items():
    if direction == 'E':
        min_score = find_shortest(n, direction, 1, been_at, min_score)
    else:
        min_score = find_shortest(n, direction, 1001, been_at, min_score)

print(f'Part 1: {min_score}')

# --- Part 2 ---

# Max score is answer to part 1
max_score = 105496 # min_score
been_at = [start.position]
paths = {start.position}

for direction, n in start.neigbour.items():
    if direction == 'E':
        paths.update(find_paths(n, direction, 1, been_at, max_score))
    else:
        paths.update(find_paths(n, direction, 1001, been_at, max_score))

print(f'Part 2: {len(paths)}')