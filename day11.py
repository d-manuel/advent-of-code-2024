with open("input/day10.txt") as f:
    s = f.read().strip()

# stones =  [125,17]
stones= [0,37551,469,63,1,791606,2065,9983586]

for x in range(75):
    i = 0
    while i < len(stones):
        stone = stones[i]
        if stone == 0: 
            stones[i] = 1 
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = str(stone)[:mid]
            right = str(stone)[mid:]
            stones[i] = int(left)
            stones.insert(i+1,int(right))
            i+=1
        else: 
            stones[i] = stone * 2024
        i+=1

print(len(stones))

