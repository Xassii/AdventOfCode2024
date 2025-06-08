# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 14:26:17 2025

@author: amanda
"""

def check_report(report):
    if report[0] - report[1] < 0:
        increase = True
    else:
        increase = False
    
    for i in range(len(report) - 1):
        if report[i] == report[i + 1]:
            return 0
        if report[i] - report[i + 1] > 3 or report[i + 1] - report[i] > 3:
            return 0
        
        if report[i] < report[i + 1] and not increase:
            return 0
        if report[i] > report[i + 1] and increase:
            return 0
    return 1

with open('Day2Input.txt') as file:
    instructions = file.readlines()

# --- Part 1 ---

result = 0

for line in instructions:
    report = line.split(' ')
    report = [int(i) for i in report]
    result += check_report(report)

print(f'Part 1: {result}')

# --- Part 2 ---

result = 0

for line in instructions:
    report = line.split(' ')
    report = [int(i) for i in report]
    
    org_result = 0
    org_result = check_report(report)
    if org_result:
        result += 1
        continue
    
    dampened_result = 0
    for i in range(len(report)):
        dampened_report = list(report)
        dampened_report.pop(i)
        dampened_result += check_report(dampened_report)
    
        if dampened_result:
            result += 1
            break

print(f'Part 2: {result}')