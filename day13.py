# type: [((int,int),(int,int),(int,int))]
grabbers = []
f = open("input/day13-modified.txt", "r")
while True:
    line = f.readline()
    print(f"line: {line}")
    print(f"line type: {type(line)}")
    if not line:
        break
    buttonA = [int(x) for x in line.split(" ")]
    print(buttonA)
    line = f.readline()
    if not line:
        break
    buttonB = [int(x) for x in line.split(" ")]
    line = f.readline()
    if not line:
        break
    goal = [int(x) for x in line.split(" ")]
    grabbers.append((buttonA, buttonB, goal))
f.close()
print(grabbers)

n, m = 100, 100


def calculate(buttonA, buttonB, goal):
    # 2d dynamic programming array
    g = [[(0, 0, 0) for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            x = buttonA[0] * i + buttonB[0] * j
            y = buttonA[1] * i + buttonB[1] * j
            cost = i * 3 + j * 1
            g[i][j] = (x, y, cost)

    cheapest = None
    for i in range(n + 1):
        for j in range(m + 1):
            # if the coordinates match the goal coordinates
            if g[i][j][0] == goal[0] and g[i][j][1] == goal[1]:
                if cheapest is None:
                    cheapest = g[i][j][2]
                    continue
                if cheapest > g[i][j][2]:
                    cheapest = g[i][j][2]
    return cheapest


res = 0
for i in range(len(grabbers)):
    maybeRes = calculate(grabbers[i][0], grabbers[i][1], grabbers[i][2])
    if maybeRes is not None:
        res += maybeRes
print(res)
