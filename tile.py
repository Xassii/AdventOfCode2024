# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 18:34:06 2025

@author: amanda
"""

import collections

class Tile:
    def __init__(self, char='', position=(0, 0)):
        self.neigbour = {}
        self.type = char
        self.position = position
        self.remember = {}
    
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


class GardenPlot(Tile):
    def __init__(self, plant):
        self.neigbour = {}
        self.fences = {}
        self.plant = plant
        self.id = 0
        self.tracker = True
#         self.explored = False
    
#     def explore_patch(self):
#         self.explored = True
#         size = 1
#         fences = 4 - len(self.neigbour)
#         
#         for n in self.neigbour.values():
#             if not n.explored and n.plant == self.plant:
#                 s, f = n.explore_patch()
#                 size += s
#                 fences += f
#             elif not n.plant == self.plant:
#                 fences += 1
        
#         return size, fences

    def explore_patch(self, num):
        self.id = num
        size = 1
        
        for direction in {'N', 'E', 'S', 'W'}:
            if not direction in self.neigbour.keys():
                self.fences[direction] = 1
            elif not self.neigbour[direction].plant == self.plant:
                self.fences[direction] = 1
            elif not self.neigbour[direction].id:
                self.fences[direction] = 0
                size += self.neigbour[direction].explore_patch(num)
            else:
                self.fences[direction] = 0
        
        return size
    
    def count_fences(self):
        self.tracker = not self.tracker
        fences = sum(self.fences.values())
        
        for direction, n in self.neigbour.items():
            if not n.tracker == self.tracker and not self.fences[direction]:
                fences += n.count_fences()
        
        return fences
    
    def count_region_sides(self, direction, check, tracking, palnt):
        result = collections.defaultdict(int)
        if not palnt == self.plant:
            tracking = []
            palnt = self.plant
        
        if check[0] in tracking and not self.fences[check[0]]:
            tracking.remove(check[0])
        if check[1] in tracking and not self.fences[check[1]]:
            tracking.remove(check[1])
        
        if not check[0] in tracking and self.fences[check[0]]:
            tracking.append(check[0])
            result[self.id] += 1
        if not check[1] in tracking and self.fences[check[1]]:
            tracking.append(check[1])
            result[self.id] += 1
        
        if not direction in self.neigbour:
            return result
        
        values = (direction, check, tracking, palnt)
        new_result = self.neigbour[direction].count_region_sides(*values)
        
        for plot_id, num in new_result.items():
            result[plot_id] += num
        
        return result