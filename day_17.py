# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:20:35 2025

@author: amanda
"""


def xdv(operand, regA, regB, regC):
    if operand <= 3:
        denominator = 2**operand
    elif operand == 4:
        denominator = 2**regA
    elif operand == 5:
        denominator = 2**regB
    elif operand == 6:
        denominator = 2**regC
    
    return int(regA / denominator)


def combo_op(operand, regA, regB, regC):
    if operand <= 3:
        return operand
    elif operand == 4:
        return regA % 8
    elif operand == 5:
        return regB % 8
    elif operand == 6:
        return regC % 8


def run_instr(opcode, operand, regA, regB, regC):
    output = ''
    
    if opcode == 0:
        regA = xdv(operand, regA, regB, regC)
    elif opcode == 1:
        regB = regB ^ operand
    elif opcode == 2:
        regB = combo_op(operand, regA, regB, regC)
    elif opcode == 3 and regA:
        return False, regA, regB, regC, ''
    elif opcode == 4:
        regB = regB ^ regC
    elif opcode == 5:
        out = combo_op(operand, regA, regB, regC)
        output = str(out)
    elif opcode == 6:
        regB = xdv(operand, regA, regB, regC)
    elif opcode == 7:
        regC = xdv(operand, regA, regB, regC)
    
    return True, regA, regB, regC, output


# 2, 4 - regB = regA % 8
# 1, 1 - regB = regB ^ 1
# 7, 5 - regC = int(regA / 2**regB)
# 4, 6 - regB = regB ^ regC
# 1, 4 - regB = regB ^ 4
# 0, 3 - regA = int(regA / 8)
# 5, 5 - out regB % 8
# 3, 0 - restart or stop
program = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
length = len(program)

# --- Part 1 ---

registerA = 59397658
registerB = 0
registerC = 0
i = 0
output = []

while i < length:
    opcode = program[i]
    operand = program[i+1]
    
    res = run_instr(opcode, operand, registerA, registerB, registerC)
    
    registerA = res[1]
    registerB = res[2]
    registerC = res[3]
    if res[4]:
        output.append(res[4])
    
    if res[0]:
        i += 2
    else:
        i = operand

print(f'Part 1: {",".join(output)}')

# --- Part 2 ---
# Is too slow to be usefull

# y = 8**16

# while True:
#     registerA = y
#     registerB = 0
#     registerC = 0
#     i = 0
#     current_num = 0
    
#     while i < length:
#         opcode = program[i]
#         operand = program[i+1]
        
#         res = run_instr(opcode, operand, registerA, registerB, registerC)
        
#         if opcode == 5 and not res[4] == str(program[current_num]):
#             break
#         if opcode == 5:
#             current_num += 1
        
#         registerA = res[1]
#         registerB = res[2]
#         registerC = res[3]
        
#         if res[0]:
#             i += 2
#         else:
#             i = operand
#     if not y % 1000000:
#         print(int(y/1000000))
#     if current_num == length:
#         break
#     y += 1

# print(f'Part 2: {y}')