with open("input/day9.txt") as f:
    s = f.read().strip()

drive = []
for i in range(len(s)):
    if (i % 2 == 0): 
        fileLength = int(s[i])
        drive.append(((i // 2),fileLength))
    else: 
        spaceSize = int(s[i])
        drive.append((None ,spaceSize))
n = len(drive)

for i in range((n - 1) // 2,-1,-1): # go over all file ids
    # find the file on the drive via the id from behind
    j = None
    for j in range(len(drive)-1,-1,-1):
        if drive[j][0] == i:
            break
    if j is None: 
        break
    for k in range(j): 
        if drive[k][0] is None and drive[k][1] >= drive[j][1]:
            oldSpace = drive[k]
            fileSize = drive[j][1]
            drive[k] = drive[j]
            drive[j] = (None, drive[j][1] )
            if oldSpace[1] >  drive[j][1]:
                drive.insert(k+1,(None,oldSpace[1]-fileSize))
            break

res = 0
resTemp = [x for x, y in drive for _ in range(y)]
for i in range(len(resTemp)):
    if resTemp[i] is not None: 
        res+=i*resTemp[i]

print(res)
