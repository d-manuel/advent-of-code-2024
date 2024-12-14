import re

type Position = tuple[int, int]
type Velocity = tuple[int, int]
type Robot = tuple[Position, Velocity]

n, m = 101, 103
robots: list[Robot] = []

with open("input/day14.txt") as f:
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


# move 100 times
for j in range(100):
    robots = [move(robot) for robot in robots]
#
# counting:
northWest = 0
southWest = 0
southEast = 0
northEast = 0
for i in range(len(robots)):
    pos = robots[i][0]
    if 0 <= pos[0] < n // 2:
        if 0 <= pos[1] < m // 2:
            northWest += 1
        elif m // 2 < pos[1] < m:
            southWest += 1
    elif n // 2 < pos[0] < n:
        if 0 <= pos[1] < m // 2:
            northEast += 1
        elif m // 2 < pos[1] < m:
            southEast += 1
print(northWest)
print(southWest)
print(southEast)
print(northEast)
print(northWest * southWest * southEast * northEast)
