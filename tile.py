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
    
    def connect_other(self, tile, direction, return_direction):
        self.neigbour[direction] = tile
        tile.neigbour[return_direction] = self


class HikingTile(Tile):
    def __init__(self, num, x=0, y=0):
        self.neigbour = {}
        self.connected_trailheads = []
        self.height = num
        self.x = x
        self.y = y
    
    def __find(self, x, y):
        if self.height == 9:
            self.connected_trailheads.append((x, y))
        
        for n in self.neigbour.values():
            if self.height + 1 == n.height:
                n.__find(x, y)
    
    def find_summit(self):
        for n in self.neigbour.values():
            if self.height + 1 == n.height:
                n.__find(self.x, self.y)