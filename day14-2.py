import re

type Position = tuple[int, int]
type Velocity = tuple[int, int]
type Robot = tuple[Position, Velocity]

n, m = 101, 103
robots: list[Robot] = []

with open("input/day14.txt") as f:
    # s = f.read().strip()
    line = f.readline()
    while line:
        nums = re.findall(r"-?\d+", line)
        robots.append(((int(nums[0]), int(nums[1])), (int(nums[2]), int(nums[3]))))
        line = f.readline()


def move(rob: Robot) -> Robot:
    pos = rob[0]
    vel = rob[1]
    newPos = ((pos[0] + vel[0]) % n, (pos[1] + vel[1]) % m)
    return (newPos, vel)


def straightLine(grid: list[list[str]]) -> bool:
    for line in grid:
        line = "".join(line)
        if 10 * "#" in line:
            return True
    return False


grid = [[" " for _ in range(n)] for _ in range(m)]
for j in range(10000):
    grid = [[" " for _ in range(n)] for _ in range(m)]
    for i in range(len(robots)):
        newRobot = move(robots[i])
        robots[i] = newRobot
        newX = newRobot[0][1]
        newY = newRobot[0][0]
        grid[newX][newY] = "#"
    if straightLine(grid):
        print(j + 1)
        break

print("\n".join("".join(line) for line in grid))
