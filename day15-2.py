# {{{ Parsing
import time

grid = []
directions = []
with open("input/day15.txt") as f:
    line = f.readline().strip()
    while line:
        if line in ["\n", "\r\n"]:
            break
        processedLine = []
        for c in line:
            if c == "#":
                processedLine.extend(["#", "#"])
            elif c == "O":
                processedLine.extend(["[", "]"])
            elif c == ".":
                processedLine.extend([".", "."])
            elif c == "@":
                processedLine.extend(["@", "."])
        grid.append(processedLine)
        line = f.readline().strip()
    line = f.readline().strip()
    while line:
        directions += list(line)
        line = f.readline().strip()
n, m = len(grid), len(grid[0])

# }}}


# {{{ Main
def findRobotPosition(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return (i, j)
    return None


def makeMove(iniPos, direction):
    direction_map = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    dx, dy = direction_map[direction]

    boxesToMove = [iniPos]
    for i, j in boxesToMove:
        newX, newY = i + dx, j + dy
        if (newX, newY) in boxesToMove:
            continue
        if grid[newX][newY] == "#":
            return iniPos
        elif grid[newX][newY] == "[":
            boxesToMove.extend([(newX, newY), (newX, newY + 1)])
        elif grid[newX][newY] == "]":
            boxesToMove.extend([(newX, newY), (newX, newY - 1)])

    # now move everything.
    # swapping from top to bottom (first to furthest box)
    for i, j in reversed(boxesToMove):
        temp = grid[i + dx][j + dy]
        grid[i + dx][j + dy] = grid[i][j]
        grid[i][j] = temp
    return (iniPos[0] + dx, iniPos[1] + dy)


def score(grid):
    score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                score += i * 100 + j
    return score


# }}}

# {{{ Final
cPos = findRobotPosition(grid)
for dir in directions:
    cPos = makeMove(cPos, dir)
    print("\n".join(["".join(line) for line in grid]), flush=True)
    time.sleep(0.0005)
print(score(grid))
