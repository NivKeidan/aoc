rocks = {}
resting_sand = {}
bottom = 0
sand_counter = 0

def add_resting_sand(x, y):
    global sand_counter, resting_sand
    if x not in resting_sand:
        resting_sand[x] = {}
    resting_sand[x][y] = True
    sand_counter += 1
    print("sand resting at (%d, %d)" % (x, y))
    # input()


def add_rock(x, y):
    if x not in rocks:
        rocks[x] = {}
    rocks[x][y] = True

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        points = l.split(" -> ")
        for j in range(len(points)-1):
            start = points[j]
            end = points[j+1]
            [sx, sy] = [int(x) for x in start.split(",")]
            [ex, ey] = [int(x) for x in end.split(",")]
            lowest_line = max(sy, ey)
            if lowest_line > bottom:
                bottom = lowest_line

            if sx == ex:
                lower = min(sy, ey)
                higher = max(sy, ey)

                for k in range(lower, higher +1,1):
                    add_rock(sx, k)
            elif sy == ey:
                lower = min(sx, ex)
                higher = max(sx, ex)
                for k in range(lower, higher + 1, 1):
                    add_rock(k, sy)
def is_free(x, y):
    if y >= bottom:
        print("cant go to (%d, %d) since it is bottom" % (x, y))
        return False
    if x in rocks and y in rocks[x]:
        print("cant go to (%d, %d) it has rock" % (x, y))
        return False
    if x in resting_sand and y in resting_sand[x]:
        print("cant go to (%d, %d) it has resting sand" % (x, y))
        return False
    print("can go to (%d, %d)" % (x, y))
    return True

def move_sand(x, y):
    print("moving sand from (%d, %d)" % (x, y))
    # if y == bottom:
    #     return False
    #     print(sand_counter)
    #     exit()
    if is_free(x, y+1):
        return move_sand(x, y+1)
    if is_free(x-1, y+1):
        return move_sand(x-1, y+1)
    if is_free(x+1, y+1):
        return move_sand(x+1, y+1)
    add_resting_sand(x, y)

bottom = bottom + 2
sandx=500
sandy=0
while is_free(500, 0):
    move_sand(sandx, sandy)
print(sand_counter)