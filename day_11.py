# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 08:05:52 2025

@author: amanda
"""

import collections

# def blink(instructions): # Too slow for part 2
#     new = []
#     for instr in instructions:
#         if instr == '0':
#             new.append('1')
#         elif len(instr) % 2:
#             new.append(str(int(instr) * 2024))
#         else:
#             middle = int(len(instr) / 2)
#             new.append(instr[:middle])
#             new.append(str(int(instr[middle:])))
    
#     return new

# def blink(instructions): # Realised I didn't need to keep track of the order. Didn't quite yet relise that ment I didn't need lists at all
#     new = []
#     counts = collections.Counter(instructions)
    
#     for value, num in counts.items():
#         if value == '0':
#             new += ['1' for x in range(num)]
#         elif len(value) % 2:
#             new_value = str(int(value) * 2024)
#             new += [new_value for x in range(num)]
#         else:
#             middle = int(len(value) / 2)
#             new_value = value[:middle]
#             new += [new_value for x in range(num)]
#             new_value = str(int(value[middle:]))
#             new += [new_value for x in range(num)]
#     return new

def blink(instructions): # Relised not needing to keep track of the order meens I can use only dictionarys...
    new = collections.defaultdict(int)
    
    for value, num in instructions.items():
        if value == '0':
            new['1'] += num
        elif len(value) % 2:
            new_value = str(int(value) * 2024)
            new[new_value] += num
        else:
            middle = int(len(value) / 2)
            new_value = value[:middle]
            new[new_value] += num
            new_value = str(int(value[middle:]))
            new[new_value] += num
    
    return new

# instructions = ['0', '37551', '469', '63', '1', '791606', '2065', '9983586'] # Bad list instruction that takes to long

# --- Part 1 ---

instructions = {'0' : 1, '37551' : 1, '469' : 1, '63' : 1, '1' : 1, '791606' : 1, '2065' : 1, '9983586' : 1}
result = 0

for i in range(25):
    instructions = blink(instructions)

for i in instructions.values():
    result += i

print(f'Part 1: {result}')

# --- Part 2 ---

instructions = {'0' : 1, '37551' : 1, '469' : 1, '63' : 1, '1' : 1, '791606' : 1, '2065' : 1, '9983586' : 1}
result = 0

for i in range(75):
    instructions = blink(instructions)

for i in instructions.values():
    result += i

print(f'Part 2: {result}')