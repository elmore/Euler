#!/usr/bin/env python3.6
from collections import namedtuple

tenToEighteen = 10000000000000000000
oposites = { "white": "black", "black": "white" }
clockwise = { "up": "right", "right": "down", "down": "left", "left": "up" }
anticlockwise = { "up": "left", "left": "down", "down": "right", "right": "up" }

def NextCoords(coords, direction):
    nextX = coords[0]
    nextY = coords[1]
    if direction == "up":
        nextY += 1
    elif direction == "right":
        nextX +=1
    elif direction == "down":
        nextY -= 1
    elif direction == "left":
        nextX -= 1 
    return (nextX, nextY)

def NextDirection(colour, direction):
    if colour == "white":
        return clockwise[direction]
    return anticlockwise[direction]

def GetColour(walk, coords):    
    if coords in walk:
        return walk[coords] 
    return "white"   

def Next(walk, coords, direction):
    # rotate
    colour = GetColour(walk, coords)
    nextDirection = NextDirection(colour, direction)
    # move
    nextCoords = NextCoords(coords, nextDirection)
    # add to walk - square we land on flips colour
    nextColour = GetColour(walk, nextCoords)
    walk[nextCoords] = oposites[nextColour]
    return (nextCoords, nextDirection)


antPosition = (0, 0)
antDirection = "up"
walk = {}
walk[antPosition] = "black"

nextAnt = (antPosition, antDirection)
for i in range(0, 10000):
    nextAnt = Next(walk, nextAnt[0], nextAnt[1])

def Depict(colour):
    if colour == "white":
        return "*"
    return " "

def Draw(walk):
    maxX =  max(pos[0] for pos in walk)
    minX =  min(pos[0] for pos in walk)
    maxY =  max(pos[1] for pos in walk)
    minY =  min(pos[1] for pos in walk)
    for y in range(maxY, minY-1, -1):
        row = "|"
        for x in range(minX, maxX+1):
            if (x,y) in walk:
                row +=  f'{Depict(walk[(x,y)])}|'
            else:
                row += '*|'
        print(row)

Draw(walk)