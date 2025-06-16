# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 19:42:39 2025

@author: amanda
"""

class GPSRobot:
    def __init__(self, tile):
        self.tile = tile
    
    def __change_if_possible(self, direction, is_at):
        if is_at.type == '.':
            return True
        if is_at.type == '#':
            return False
        
        move_to = is_at.neigbour[direction]
        possible = self.__change_if_possible(direction, move_to)
        
        if possible:
            is_at.neigbour[direction].type = is_at.type
        return possible
        
    def move(self, direction):
        move_to = self.tile.neigbour[direction]
        possible = self.__change_if_possible(direction, move_to)
        
        if possible:
            self.tile.type = '.'
            self.tile = move_to
            self.tile.type = '@'
    
    def __check_possible(self, direction, is_at):
        if is_at.type == '.':
            return True
        if is_at.type == '#':
            return False
        
        move_to = is_at.neigbour[direction]
        possible = self.__check_possible(direction, move_to)
        if not possible:
            return possible
        
        if is_at.type == '[':
            split_to = is_at.neigbour['E'].neigbour[direction]
        else:
            split_to = is_at.neigbour['W'].neigbour[direction]
        
        if split_to.type == '#':
            return False
        elif not split_to.type == '.':
            possible = self.__check_possible(direction, split_to)
        
        return possible
    
    def __change(self, direction, is_at):
        if is_at.type == '.':
            return None
        
        self.__change(direction, is_at.neigbour[direction])
        if is_at.type == '[':
            split_to = is_at.neigbour['E']
        else:
            split_to = is_at.neigbour['W']
        if not split_to.neigbour[direction].type == '.':
            self.__change(direction, split_to.neigbour[direction])
        
        is_at.neigbour[direction].type = is_at.type
        is_at.type = '.'
        split_to.neigbour[direction].type = split_to.type
        split_to.type = '.'
    
    def wide_move(self, direction):
        move_to = self.tile.neigbour[direction]
        if move_to.type == '.':
            self.tile.type = '.'
            self.tile = move_to
            self.tile.type = '@'
            return None
        
        if direction == 'N' or direction == 'S':
            possible = self.__check_possible(direction, move_to)
        else:
            possible = self.__change_if_possible(direction, move_to)
        
        if possible:
            if direction == 'N' or direction == 'S':
                self.__change(direction, move_to)
            self.tile.type = '.'
            self.tile = move_to
            self.tile.type = '@'