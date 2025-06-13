# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:09:51 2025

@author: amanda
"""

class DirectionlesTile:
    def __init__(self):
        self.neigbour = []
    
    def connect_tile(self, other_tile):
        self.neigbour.append(other_tile)
        other_tile.neigbour.append(self)


class HikingTile(DirectionlesTile):
    def __init__(self, num, x=0, y=0):
        self.neigbour = []
        self.connected_trailheads = []
        self.height = num
        self.x = x
        self.y = y
    
    def __find(self, x, y):
        if self.height == 9:
            self.connected_trailheads.append((x, y))
        
        for n in self.neigbour:
            if self.height + 1 == n.height:
                n.__find(x, y)
    
    def find_summit(self):
        for n in self.neigbour:
            if self.height + 1 == n.height:
                n.__find(self.x, self.y)