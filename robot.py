# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 10:36:54 2025

@author: amanda
"""

class Robot:
    def __init__(self, tile, speed):
        self.possition = tile
        self.speed = speed
    
    def move(self):
        self.possition.type -= 1
        
        if self.speed[0] > 0:
            direction = 'E'
        elif self.speed[0] < 0:
            direction = 'W'
        else:
            direction = ''
        
        if direction:
            for i in range(abs(self.speed[0])):
                self.possition = self.possition.neigbour[direction]
        
        if self.speed[1] > 0:
            direction = 'S'
        elif self.speed[1] < 0:
            direction = 'N'
        else:
            direction = ''
        
        if direction:
            for i in range(abs(self.speed[1])):
                self.possition = self.possition.neigbour[direction]
        
        self.possition.type += 1