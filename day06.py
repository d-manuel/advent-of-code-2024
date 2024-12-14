#!/usr/bin/env python

from enum import Enum
import copy

def loadGrid():
    f = open("input/day6-padded.txt","r") 
    grid =  f.readlines()
    grid = list(map(lambda line: list(line.strip()), grid))
    return grid

# added padding with vim

class Direction(Enum):
    NORTH = [-1,0]
    EAST  = [0, 1]
    SOUTH = [1,0]
    WEST  = [0,-1]

def nextDirection(direction:Direction):
    if direction == Direction.NORTH:
        return Direction.EAST
    if direction == Direction.EAST:
        return Direction.SOUTH
    if direction == Direction.SOUTH:
        return Direction.WEST
    if direction == Direction.WEST:
        return Direction.NORTH

def startingPosition(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                return [i,j]
    return None  # Element not found

def calculate(inputGrid, startingPosition):
    grid = inputGrid
    direction = Direction.NORTH
    position = startingPosition
    distinct_count = 1
    while True:
        while True: 
            newPosition = [position[0]+direction.value[0],position[1]+direction.value[1]]
            if grid[newPosition[0]][newPosition[1]] == "#":
                direction = nextDirection(direction)
                continue
            position = newPosition
            #print(newPosition[0]+1,newPosition[1]+1)
            break
        if grid[position[0]][position[1]] == "0":
            break # we left the grid!
        if grid[position[0]][position[1]] != 1:
            distinct_count=distinct_count+1
            grid[position[0]][position[1]] = 1
    return distinct_count

grid = loadGrid()
sPos = startingPosition(grid)
print("solution part 1:")
print(calculate(grid,sPos))

# part 2
# idea. for all positions, put a obstacle there (add a #), simulate the run and then check if get's stuck. 
# maybe there would be an algorithmically better solution. backtrackicng, graph algorihtms etc. 
#

# check if the guard would get stuck in a loop
def checkLoop(inputGrid, startPosition):
    grid = inputGrid # make a new grid to reuse the old one as a template. 
    # I don't know if python does call by value of reference in this scenario.
    
    direction = Direction.NORTH
    position = startPosition
    visited = {Direction.NORTH: [], Direction.EAST : [], Direction.SOUTH : [], Direction.WEST : []}
    while True:
        while True: # determine next position
            newPosition = [position[0]+direction.value[0],position[1]+direction.value[1]]
            if grid[newPosition[0]][newPosition[1]] == "#":
                direction = nextDirection(direction)
                continue
            position = newPosition
            #print(newPosition[0]+1,newPosition[1]+1)
            break
        if grid[position[0]][position[1]] == "0":
            return False # we left the grid, now loop!

        if position in visited[Direction.NORTH] and direction == Direction.NORTH:
            print("revisited NORTH ways")
            return True;
        if position in visited[Direction.EAST] and direction == Direction.EAST:
            print("revisited EAST ways")
            return True;
        if position in visited[Direction.SOUTH] and direction == Direction.SOUTH:
            print("revisited SOUTH ways")
            return True;
        if position in visited[Direction.WEST] and direction == Direction.WEST:
            print("revisited WEST ways")
            return True;
        if grid[position[0]][position[1]] == "." or grid[position[0]][position[1]] == "^":
            visited[direction].append(position)
            continue
        print(grid[position[0]][position[1]])
        raise Exception("Error in the Grid") 

# ignore starting position for a possible obstacle!

def calculate2(grid, startingPosition):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                print(f"place obstacle at:{i,j}")
                if checkLoop(grid,startingPosition):
                    count=count+1
                grid[i][j] = "."
    return count

grid = loadGrid()
sPos = startingPosition(grid)
print("solution part 2:")
calculate2(grid,sPos)

# Reflection where I might have lost performance:
# - Index of visited being enums
# - The visited datastructure is chosen badly anyway. Way to complex for 
#   for this simple lookup of triples x,y and direction
# - more string comparisions because of padding instead of x in range(m)
