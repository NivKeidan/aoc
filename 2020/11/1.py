FLOOR = "."
EMPTY = "L"
TAKEN = "#"

grid = []

debug = False
# round_num = 5

def count_occs(i, j):
    global debug
    
    if i == 0 and j == 3:
        debug = True
    
    if debug: print("counting occs for", i, j)
    cnt = 0

    changes =[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
    for c in changes:
        new_i = i
        new_j = j
        while True:
            new_i = new_i + c[0]
            new_j = new_j + c[1]
            if debug: print("checking", new_i, new_j)
            if new_i < 0 or new_j < 0:
                if debug: print("one index less than zero")
                # cant go further, we are at edge
                break
            try:
                if grid[new_i][new_j] == TAKEN:
                    if debug: print("taken")
                    cnt += 1
                    break
                if grid[new_i][new_j] == EMPTY:
                    if debug: print("empty")
                    break
            except IndexError:
                if debug: print("out of bounds")
                break
    debug = False
    return cnt

def new_value(i, j):
    v = grid[i][j]
    
    if v == FLOOR:
        return FLOOR

    occs = count_occs(i, j)
    if v == EMPTY and occs == 0:
        return TAKEN
    
    if v == TAKEN and occs >= 5:
        return EMPTY
    return v

def get_next_round_grid():
    new_grid = []

    for i in range(0, len(grid)):
        new_row = ""
        for j in range(0, len(grid[0])):
            new_row += new_value(i, j)
        new_grid.append(new_row)
    return new_grid

def showGrid():
    for row in grid:
        print(row)

def count_occs_general():
    c = 0
    
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == TAKEN:
                c += 1
    return c

def is_changed(grid2):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid2[i][j] != grid[i][j]:
                return True
    return False

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        grid.append(l)

i = 0
while True:
    print("round", i)
    showGrid()
    # input()
    new_grid = get_next_round_grid()
    if not is_changed(new_grid):
        print(count_occs_general())
        exit()
    grid = new_grid
    i += 1