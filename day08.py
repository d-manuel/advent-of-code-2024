from collections import defaultdict
from enum import unique
from pprint import pp, pprint; 
with open("input/day8.txt") as f:
    s = f.read().strip()

in1 = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

grid = [list(r) for r in s.split('\n')]
n, m = len(grid), len(grid[0])

ans = res = 0

ix,iy = 0, 0  

explored = defaultdict(list)

for x in range(n): 
    for y in range(m):
        freq = grid[x][y]
        if freq != ".":
            explored[freq].append((x,y))
 
pprint(explored)
def locDiff(loc1, loc2):
    return (loc1[0]-loc2[0], loc1[1]-loc2[1])
def neg(loc):
    return((-1*loc[0],-1*loc[1]))
def locAdd(loc,diff):
    return((loc[0]+diff[0],loc[1]+diff[1]))


uniqueLocs = set()
for freq, locs in explored.items(): 
    for x in range(len(locs)):
        for y in range(x+1,len(locs)):
            loc1 = locs[x]
            loc2 = locs[y]
            pprint(f"{loc1},{loc2}")
            d = locDiff(loc1,loc2)
            pprint(f"d:{d}")
            antiNodeLocation = loc1
            while (antiNodeLocation[0] in range(n) and antiNodeLocation[1] in range(m)):
                pprint(f"antiNodeLocation1: {antiNodeLocation}")
                uniqueLocs.add(antiNodeLocation)
                antiNodeLocation = locAdd(antiNodeLocation,d)
            antiNodeLocation = loc1
            while (antiNodeLocation[0] in range(n) and antiNodeLocation[1] in range(m)):
                pprint(f"antiNodeLocation1: {antiNodeLocation}")
                uniqueLocs.add(antiNodeLocation)
                antiNodeLocation = locAdd(antiNodeLocation,neg(d))
pprint(f"count:{len(uniqueLocs)}")
# pprint(f"{uniqueLocs}")
