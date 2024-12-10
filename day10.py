with open("input/day10.txt") as f:
    s = f.read().strip()

grid = [[int(x) for x in list(r)] for r in s.split('\n')]
n, m = len(grid), len(grid[0])

def traverse(x,y):
    visited = set()
    q = [(x,y)]
    count = 0
    if grid[x][y] != 0:
        return 0
    while q: 
        x, y = q.pop(0)
        if (x,y) in visited: 
            continue
        else: 
            visited.add((x,y))
        if grid[x][y] == 9:
            count+=1
            continue
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= x+dx < n and 0 <= y+dy < m and grid[x][y] +1 == grid[x+dx][y+dy]:
                q.append((x+dx,y+dy))
    return count


res = sum([traverse(i,j) for i in range(n) for j in range(m)])
print(res)
