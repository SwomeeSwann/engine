import re
from enum import Enum
import pygame

result = re.split(" ", "LOAD 0 1")

registers = [0, 0, 0, 0, 0, 0, 0, 0]

class instructions(Enum):
    LOAD = 0
    STORE = 1
    ADD = 2
    SUB = 3
    DSQU = 4
    LOOP = 5
    
  
def execute(result):
    if result[0] == "LOAD":
        opcode = instructions.LOAD.value
        registers[int(result[1])] = int(result[2])
    elif result[0] == "STORE":
        opcode = instructions.STORE.value
        registers[int(result[2])] = int(result[1])
    elif result[0] == "ADD":
        opcode = instructions.ADD.value
        registers[int(result[1])] += registers[int(result[2])]
    elif result[0] == "SUB":
        opcode = instructions.SUB.value
        registers[int(result[1])] -= registers[int(result[2])]
    elif result[0] == "DSQU":
        from main import screen
        pygame.draw.rect(screen, result[1], pygame.Rect(int(result[2]), int(result[3]), int(result[4]), int(result[4])))
        opcode = instructions.DSQU.value
    elif result[0] == "LOOP":
        opcode = instructions.LOOP.value
    else:
        return None
    
    
    return opcode
    
    
def read():
    
    file = open("file.sw", "r")

    
    for x in file:
        opcode = execute(re.split(" ", x.rstrip()))
            

