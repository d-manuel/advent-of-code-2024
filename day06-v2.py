with open("input/day6.txt") as f:
    s = f.read().strip()

ans = res = 0
# grid
grid = [list(r) for r in s.split('\n')]
n, m = len(grid), len(grid[0])

ix,iy = 0, 0  # initial position of guard in the grid

# Determine starting position
for x in range(n): 
    for y in range(m):
        if grid[x][y] in "^<>v": 
            print(grid[x][y])
            ix,iy = x, y

directions = [(-1,0),(0,1),(1,0),(0,-1)]

for ox in range(n):
    for oy in range(m):
        print(ox,oy)
        if grid[ox][oy] == "#" or grid[ox][oy] == "^":
            continue;

        # add obstruction
        grid[ox][oy] = "#"

        seen = set()
        
        cd = 0 # index of the last seen direction
        cx, cy = ix, iy # current position of the guard

        while cx in range(n) and cy in range(m) and (cx,cy,cd) not in seen: 
            seen.add((cx,cy,cd))
            while True:
                cdir = directions[cd]
                nx, ny = cx + cdir[0], cy + cdir[1]
                if nx in range(n) and ny in range(m) and grid[nx][ny] == "#":
                    cd = (cd + 1) % 4
                else: 
                    cx,cy = nx, ny
                    break

        if (cx,cy,cd) in seen: 
            ans += 1

        # reset obstruction
        grid[ox][oy] = "."
print(ans)




