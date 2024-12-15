from pprint import pprint

grid: list[list[str]] = []
directions: list[str] = []
with open("input/day15.txt") as f:
    line = f.readline().strip()
    while line:
        if line in ["\n", "\r\n"]:
            break
        grid.append(list(line))
        line = f.readline().strip()
    line = f.readline().strip()
    while line:
        directions += list(line)
        line = f.readline().strip()


def findRobotPosition(grid: list[list[str]]) -> tuple[int, int] | None:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)
    return None


# assuming grid as a global variable that is modified. I should probably design this
# OO with classes
# type safety that str is element of <>^v would be nice. enum or something
#
# Input: robot position and the direction.
# It returns the new Position of the robot
def makeMove(pos: tuple[int, int], direction: str) -> tuple[int, int]:
    direction_map = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    dir = direction_map.get(direction, (0, 0))

    advance = lambda p, d: (p[0] + d[0], p[1] + d[1])
    # breakpoint()
    t = advance(pos, dir)
    while grid[t[0]][t[1]] == "O":
        t = advance(t, dir)
    # If we cannot push the boxes due to a wall we do nothing
    if grid[t[0]][t[1]] == "#":
        return pos
    # If there is space, we push all the boxes one space over, which
    # is equivalent to swapping the current box to that position, because
    # all the boxes are equal!
    if grid[t[0]][t[1]] == ".":
        grid[pos[0]][pos[1]] = "."
        grid[t[0]][t[1]] = "O"
        firstNeighbor = advance(pos, dir)
        grid[firstNeighbor[0]][firstNeighbor[1]] = "@"
        return firstNeighbor
    return pos


# sum of gps locations with multipliers 100 and 1
def score(grid: list[list[str]]) -> int:
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                score += i * 100 + j
    return score


pos = findRobotPosition(grid)
for dir in directions:
    if pos == None:
        continue
    pos = makeMove(pos, dir)
