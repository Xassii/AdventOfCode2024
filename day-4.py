# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 08:01:08 2025

@author: amanda
"""

import numpy

with open('Day4Input.txt') as file:
    instructions = file.read().split('\n')
    
# --- Part 1 ---
"""
test = numpy.array([['a', 'b'], ['c', 'd']])
print(test)
a = numpy.rot90(test)
print(a)
b = test.diagonal(1)
print(b)
"""

result = 0

instructions = [list(x) for x in instructions]
word_search = numpy.array(instructions)
word_search = numpy.rot90(word_search)

print(f'Part 1: {result}')

# --- Part 2 ---

#result = 0



#print(f'Part 2: {result}')