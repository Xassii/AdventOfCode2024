# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 18:23:19 2025

@author: amanda
"""

class Guard:
    def __init__(self, tile):
        self.facing = 'N'
        self.start_tile = tile
        self.is_at = tile
        self.has_been_at = []
    
    def return_to_start(self):
        self.facing = 'N'
        self.is_at = self.start_tile
        self.has_been_at = []
    
    def turn(self):
        if self.facing == 'N':
            self.facing = 'E'
        elif self.facing == 'E':
            self.facing = 'S'
        elif self.facing == 'S':
            self.facing = 'W'
        elif self.facing == 'W':
            self.facing = 'N'
    
    def move(self):
        forward = self.is_at.neigbour[self.facing]
        if forward.type == '#' or forward.type == 'O':
            self.turn()
        else:
            self.is_at = forward
    
    def move_to_end(self):
        self.is_at.type = 'X'
        if not self.facing in self.is_at.neigbour.keys():
            return False
        
        self.move()
        return True
    
    def move_to_loop(self):
        if not self.facing in self.is_at.neigbour.keys():
            return False, False
        
        forward = self.is_at.neigbour[self.facing]
        if forward.type == '#' or forward.type == 'O':
            for place in self.has_been_at:
                if place[0] is self.is_at and place[1] == self.facing:
                    return True, True
            
            self.has_been_at.append([self.is_at, self.facing])
        
        self.move()
        return True, False