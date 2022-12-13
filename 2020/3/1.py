map = []

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        row = l
        map.append(l)

lastRow = len(map)-1
lastCol = len(map[0])-1

def isTree(x, y):
    return map[x][y] == '#'

def runSlope(xChange, yChange):
    xCurrent = 0
    yCurrent = 0
    treeCount = 0

    while xCurrent <= lastRow:
        print("now in (%d,%d)" % (xCurrent, yCurrent))
        if yCurrent > lastCol:
            newY = yCurrent % (lastCol+1)
            print("changing %d to %d" % (yCurrent, newY))
            yCurrent = newY
        if isTree(xCurrent, yCurrent):
            treeCount += 1
        xCurrent += xChange
        yCurrent += yChange
    return treeCount

slops = [(1,1), (1,3), (1, 5), (1, 7), (2, 1)]
t = 1
for slope in slops:
    c = runSlope(slope[0], slope[1])
    print(c)
    t *= c
print(t)
