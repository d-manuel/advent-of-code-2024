# type: [((int,int),(int,int),(int,int))]
grabbers = []
f = open("input/day13-modified.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    buttonA = [int(x) for x in line.split(" ")]
    line = f.readline()
    if not line:
        break
    buttonB = [int(x) for x in line.split(" ")]
    line = f.readline()
    if not line:
        break
    goal = [int(x) + 10000000000000 for x in line.split(" ")]
    grabbers.append((buttonA, buttonB, goal))
f.close()


def calculate(buttonA: list[int], buttonB: list[int], goal: list[int]):
    j = (buttonA[0] * goal[1] - buttonA[1] * goal[0]) / (
        buttonA[0] * buttonB[1] - buttonA[1] * buttonB[0]
    )
    i = (goal[0] - j * buttonB[0]) / buttonA[0]
    if i % 1 == 0 and j % 1 == 0:
        return int(i * 3 + j)
    return None


res = 0
count = 0
for i in range(len(grabbers)):
    print(i)
    maybeRes = calculate(grabbers[i][0], grabbers[i][1], grabbers[i][2])
    if maybeRes is not None:
        count += 1
        res += maybeRes
print(res)
print(count)
