from collections import defaultdict


with open("input/day9.txt") as f:
    s = f.read().strip()

drive = []

for i in range(len(s)):
    if (i % 2 == 0): 
        fileLength = int(s[i])
        # print(fileLength)
        drive = drive + (fileLength *[i//2])
    else: 
        space = int(s[i])
        drive = drive + (space * [None])
        # print(space)

def remove_first_non_none_from_rear(lst,ind):
    for i, item in reversed(list(enumerate(lst))):
        if i <= ind:
            break
        if item is not None:
            return lst[:i] + lst[i+1:], item
    return lst, None
i = 0
while True :
    #     breakpoint()
    if drive[i] == None:
        # drop first from the back of the list
        # drive, el = remove_first_non_none_from_rear(drive)
        drive, el = remove_first_non_none_from_rear(drive,i)
        drive[i] = el
    print(f"iteration{ i} from {len(drive)}")
    i+=1
    if i >= len(drive):
        break;

res = 0
for i in range(len(drive)):
    if drive[i] == None:
        break
    res+=i*drive[i]
    print(f"iteration{ i} from {len(drive)}")

# print(drive)
print(res)
