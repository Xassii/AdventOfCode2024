# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 15:57:38 2025

@author: amanda
"""


def find_max_b(a, b, goal, times_a, times_b):
    x = a[0] * times_a + b[0] * times_b
    y = a[1] * times_a + b[1] * times_b
    
    if x == goal[0] and y == goal[1]:
        return [[times_a, times_b]]
    if x > goal[0] or y > goal[1]:
        return []
    
    result = find_max_b(a, b, goal, times_a, times_b + 1)
    
    return result


def find_max_a(a, b, goal, times_a, times_b):
    x = a[0] * times_a + b[0] * times_b
    y = a[1] * times_a + b[1] * times_b
    
    if x == goal[0] and y == goal[1]:
        return [times_a, times_b]
    if x > goal[0] or y > goal[1]:
        return []
    
    result = find_max_a(a, b, goal, times_a + 1, times_b)
    result += find_max_b(a, b, goal, times_a, times_b + 1)
    
    return result


with open('Day13Input.txt') as file:
    instructions = file.read().split('\n')

machines = [{}]
i = 0

for line in instructions:
    if not line:
        machines.append({})
        i += 1
    elif line[0] == 'P':
        machines[i]['P'] = [int(x) for x in line[9:].split(', Y=')]
    elif line[7] == 'A':
        machines[i]['A'] = [int(x) for x in line[12:].split(', Y+')]
    else:
        machines[i]['B'] = [int(x) for x in line[12:].split(', Y+')]

# --- Part 1 ---
# Didn't feel like doing math today

result = 0

for machine in machines:
    combi = find_max_a(machine['A'], machine['B'], machine['P'], 0, 0)
    
    costs = []
    for way in combi:
        costs.append(way[0] * 3 + way[1])
    
    if costs:
        result += min(costs)

print(f'Part 1: {result}')

# --- Part 2 ---
# Had to do math anyway

result = 0

for machine in machines:
    p1, p2 = [x + 10000000000000 for x in machine['P']]
    a1, a2 = machine['A']
    b1, b2 = machine['B']
    
    times1 = (a2 * p1 - a1 * p2) / (a2 * b1 - a1 * b2)
    if not times1 - int(times1):
        times2 = (p1 - b1 * times1)/a1
        if not times2 - int(times2):
            result += int(times2 * 3 + times1)

print(f'Part 2: {result}')