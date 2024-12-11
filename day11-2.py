from collections import Counter


stones= [0,37551,469,63,1,791606,2065,9983586]

counter = Counter(stones)

for _ in range(75):
    newCounter =  Counter()
    for i in counter:
        if i == 0: 
            newCounter[1] += counter[i]
        elif len(str(i)) % 2 == 0:
            mid = len(str(i)) // 2
            left = str(i)[:mid]
            right = str(i)[mid:]
            newCounter[int(left)] += counter[i]
            newCounter[int(right)] += counter[i]
        else: 
            newCounter[i*2024] += counter[i]
    counter = newCounter
print(counter.total())
