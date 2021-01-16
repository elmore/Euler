#!/usr/bin/env python3.6

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
    # determine current square colour
    colour = GetColour(walk, coords)
    # rotate
    nextDirection = NextDirection(colour, direction)
    # flip colour
    walk[coords] = oposites[colour]
    # move
    nextCoords = NextCoords(coords, nextDirection)
    # return new location and direction
    return (nextCoords, nextDirection)

def Run(number):
    colours = {}
    walk = []
    directions = []
    ant = ((0, 0), 'up')
    for i in range(0, number):
        ant = Next(colours, ant[0], ant[1])
        walk.append(ant[0])
        directions.append(ant[1])
    return (colours, walk, directions)