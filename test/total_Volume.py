def totalVolume(*box):
    vol = 0
    for i in box:
        vol = vol + (i[0]*i[1]*i[2])
    return vol


print(totalVolume([4,2,4],[3,3,3],[1,1,2],[2,1,1]))
print(totalVolume([2,2,2],[2,1,1]))
print(totalVolume([1,1,1]))