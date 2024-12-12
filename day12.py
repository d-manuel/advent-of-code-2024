with open("input/day12.txt") as f:
    s = f.read().strip()

grid = [list(r) for r in s.split('\n')]
n, m = len(grid), len(grid[0])

def traverse(x,y):
    visited = set()
    q = [(x,y)]
    region = set() # a new region is a set of positions
    while q: 
        x, y = q.pop(0)
        if (x,y) in visited: 
            continue
        visited.add((x,y))
        region.add((x,y))
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= x+dx < n and 0 <= y +dy < m and grid[x][y] == grid[x+dx][y+dy] and (x+dx,y+dy) not in visited:
                q.append((x+dx,y+dy))
    return region

processed= set() # keep track of positions that are added to a garden region
regions = []
for x in range(n):
    for y in range(m):
        if (x,y) in processed:
            continue
        region = traverse(x,y)
        if len(region) > 0:
            regions.append(region)
            processed = processed.union(region)

def regionPrice(region):
    area = len(region)
    perimeter = 0
    for x,y  in region:
        numNeighbours = 0
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if (x+dx,y+dy) in region:
                numNeighbours+=1
        perimeter += 4-numNeighbours
    return area*perimeter

res = sum([regionPrice(r) for r in regions])
print(f"part 1: {res}")


########## Part 2 ##########

def regionPrice2(region):
    # Calculate the number of corners of the plot. This is equal to the number of sides
    corners = 0
    area = len(region)
    for pos in region:
        for dx, dy in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
            if ((pos[0]+dx, pos[1]) not in region and (pos[0], pos[1]+dy) not in region):
                corners += 1
            if ((pos[0]+dx, pos[1]) in region and (pos[0], pos[1]+dy) in region and (pos[0]+dx, pos[1]+dy) not in region):
                 corners += 1

    price = corners*area
    return price

res2 = sum([regionPrice2(r) for r in regions])
print(f"part 2: {res2}")
