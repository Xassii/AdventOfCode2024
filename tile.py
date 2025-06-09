# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 18:34:06 2025

@author: amanda
"""

class Tile:
    def __init__(self, char):
        self.neigbour = {}
        self.type = char
    
    def connect_neigbour(self, neigbour, direction):
        self.neigbour[direction] = neigbour
        if direction == 'N':
            neigbour.neigbour['S'] = self
        elif direction == 'E':
            neigbour.neigbour['W'] = self
        elif direction == 'S':
            neigbour.neigbour['N'] = self
        elif direction == 'W':
            neigbour.neigbour['E'] = self