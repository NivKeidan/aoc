file_name = "./9/inp"

low_points = []

    
def make_grid():
    grid = []
    with open(file_name) as f:
        for l in f.readlines():
            l = l.strip()
            grid.append(l)
        return grid

g = make_grid()

def getNeighbours(row, col):
    global g
    options = [(row+1, col), (row, col+1), (row-1,col), (row, col-1)]
    finals = []
    for o in options:
        (x, y ) = o
        if x < 0 or y < 0 or x > len(g)-1 or y > len(g[0])-1:
            continue
        finals.append(g[x][y])
    return finals



for i, row in enumerate(g):
    for j, cell in enumerate(row):
        valid = True
        nbors = getNeighbours(i, j)

        for n in nbors:
            if int(n) <= int(cell):
                valid = False
                break
        if valid:
            print(i,j)
            low_points.append(cell)

print(low_points)
s = 0
for lp in low_points:
    s += int(lp)
print(s+len(low_points))

