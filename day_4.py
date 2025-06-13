# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 08:01:08 2025

@author: amanda
"""

import tile


def search_word(is_at, direction, word):
    count = 0
    found_word = ''
    on_char = 0
    while True:
        if is_at.type == word[on_char]:
            found_word += is_at.type
            on_char += 1
        else:
            found_word = ''
            on_char = 0
        
            if is_at.type == word[on_char]:
                found_word += is_at.type
                on_char += 1
        
        if found_word == word:
            count += 1
            found_word = ''
            on_char = 0
        
        if not direction in is_at.neigbour.keys():
            return count
        
        is_at = is_at.neigbour[direction]


def search_x(tile, word):
    if not tile.type == word[1]:
        return 0
    
    ne = tile.neigbour['NE']
    nw = tile.neigbour['NW']
    se = tile.neigbour['SE']
    sw = tile.neigbour['SW']
    
    word1 = ne.type == word[0] and sw.type == word[2]
    word1 = word1 or ne.type == word[2] and sw.type == word[0]
    if word1:
        word2 = nw.type == word[0] and se.type == word[2]
        word2 = word2 or nw.type == word[2] and se.type == word[0]
        if word2:
            return 1
    
    return 0


with open('Day4Input.txt') as file:
   instructions = file.read().split('\n')

word_serch = []

for x, row in enumerate(instructions):
    word_serch.append([])
    for y, char in enumerate(row):
        word_serch[x].append(tile.Tile(char))
        new = word_serch[x][y]
        if x > 0:
            new.connect_neigbour(word_serch[x - 1][y], 'N')
        if y > 0:
            new.connect_neigbour(word_serch[x][y - 1], 'W')
        if x > 0 and y > 0:
            new.connect_other(word_serch[x - 1][y - 1], 'NW', 'SE')
        if x > 0 and y < len(instructions[0]) - 1:
            new.connect_other(word_serch[x - 1][y + 1], 'NE', 'SW')

# --- Part 1 ---

result = 0
corners = [word_serch[0][0], word_serch[0][-1]]
corners = corners + [word_serch[-1][0], word_serch[-1][-1]]
edges_top_bottom = word_serch[0][1:-1] + word_serch[-1][1:-1]
edges_sides = [x[0] for x in word_serch[1:-1]]
edges_sides = edges_sides + [x[-1] for x in word_serch[1:-1]]

for corner in corners:
    for direction in corner.neigbour.keys():
        result += search_word(corner, direction, 'XMAS')
for side in edges_sides:
    directions = list(side.neigbour.keys())
    directions.remove('N')
    directions.remove('S')
    for direction in directions:
        result += search_word(side, direction, 'XMAS')
for side in edges_top_bottom:
    directions = list(side.neigbour.keys())
    directions.remove('E')
    directions.remove('W')
    for direction in directions:
        result += search_word(side, direction, 'XMAS')

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0
middle = [x[1:-1] for x in word_serch[1:-1]]

for x in middle:
    for y in x:
        result += search_x(y, ['M', 'A', 'S'])

print(f'Part 2: {result}')