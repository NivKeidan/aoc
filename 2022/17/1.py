DIR_3R = "3r"
DIR_3L = "3l"
DIR_1R = "1r"
DIR_1L = "1l"
EMPTY_ROW = "......."
current_rock_locations = {}
chamber = []
rock_i = 0
gas_i = 0
rock_stop_limit = 2022
width = 7
rock_stop_counter = 0
indxs = {}
gases = ""

class Rock:
    def __init__(self, data, d1r, d3r, d1l, d3l) -> None:
        self.data = data
        self.d1r = d1r
        self.d1l = d1l
        self.d3r = d3r
        self.d3l = d3l
    
    def get_post_move(self, d):
        if d == DIR_1R:
            return self.d1r
        if d == DIR_3R:
            return self.d3r
        if d == DIR_1L:
            return self.d1l
        if d == DIR_3L:
            return self.d3l
    
rocka = Rock(
    ["..####."],
    ["...####"],
    ["...####"],
    [".####.."],
    ["####..."]
)
rockb = Rock(
    ["...#...", "..###..", "...#..."],
    ["....#..", "...###.", "....#.."],
    ["......#", "....###", "......#"],
    ["..#....", ".###...", "..#...."],
    [".#.....", "###....", ".#....."]
)
rockc = Rock(
    [ "....#..", "....#..", "..###.." ],
    [ ".....#.", ".....#.", "...###." ],
    [ "......#", "......#", "....###" ],
    [ "...#...", "...#...", ".###..." ],
    [ "..#....", "..#....", "###...." ],
)
rockd = Rock(
    ["..#....", "..#....", "..#....", "..#...."],
    ["...#...", "...#...", "...#...", "...#..."],
    [".....#.", ".....#.", ".....#.", ".....#."],
    [".#.....", ".#.....", ".#.....", ".#....."],
    ["#......", "#......", "#......", "#......"],
)
rocke = Rock(
    ["..##...", "..##..."],
    ["...##..", "...##.."],
    [".....##", ".....##"],
    [".##....", ".##...."],
    ["##.....", "##....."],
)
rocks = [rocka, rockb, rockc, rockd, rocke]

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def get_left(row):
    indxs = find(row, "#")
    new_r = list(row)
    for i in indxs:
        if i == 0:
            break
        new_r[i-1] = "#"
        new_r[i] = "."
    return "".join(new_r)

def get_right(row):
    indxs = find(row, "#")
    new_r = list(row)
    for i in reversed(indxs):
        if i == len(new_r)-1:
            break
        new_r[i+1] = "#"
        new_r[i] = "."
    return "".join(new_r)

def get_indxs(r):
    global indxs
    if r not in indxs:
        indxs[r] = find(r, "#")
    return indxs[r]

def set_row_empty(i):
    set_row(i, EMPTY_ROW)

def set_row(i, d):
    global chamber
    if i < len(chamber):
        chamber[i] = d
    elif i == len(chamber):
        chamber.append(d)
    else:
        raise Exception("trying to add row in index %d when chamber has %d rows" % (i, len(chamber)))

def get_highest_rock_row():
    for i in range(len(chamber)-1, -1, -1):
        r = chamber[i]
        if r != EMPTY_ROW:
            return i
    return -1

def move_rock_locations_down():
    global current_rock_locations
    new_loc = {}
    for k, v in current_rock_locations.items():
        new_loc[k-1] = v
    current_rock_locations = new_loc

def move_rock_locations_left():
    global current_rock_locations
    new_loc = {}
    for k, v in current_rock_locations.items():
        new_loc[k] = [x-1 for x in v]
    current_rock_locations = new_loc

def move_rock_locations_right():
    global current_rock_locations
    new_loc = {}
    for k, v in current_rock_locations.items():
        new_loc[k] = [x+1 for x in v]
    current_rock_locations = new_loc

def move_rock_left():
    global chamber
    # print("moving rock left")
    if not can_move_left():
        return

    for r, indexes in current_rock_locations.items():
        new_r = list(chamber[r])
        for i in indexes:
            new_r[i-1] = "#"
            new_r[i] = "."
        chamber[r] = "".join(new_r)
    
    move_rock_locations_left()

def can_move_left():
    global current_rock_locations, chamber
    for r, indexes in current_rock_locations.items():
        i = min(indexes)
        if i == 0:  # rock at left edge
            return False
        if chamber[r][i-1] == "#":
            return False  # rock to the left
    return True

def move_rock_right():
    global chamber
    # print("moving rock right")
    
    if not can_move_right():
        return
    
    for r, indexes in current_rock_locations.items():
        new_r = list(chamber[r])
        for i in reversed(indexes):
            new_r[i+1] = "#"
            new_r[i] = "."

        chamber[r] = "".join(new_r)
    
    move_rock_locations_right()

def can_move_right():
    global current_rock_locations, chamber
    for r, indexes in current_rock_locations.items():
        i = max(indexes)
        if i == width-1:  # rock at right edge
            return False
        if chamber[r][i+1] == "#":
            return False  # rock to the right
    return True

def merge_rows(r1, r2):
    new_r = []
    for i in range(len(r1)):
        if r1[i] == r2[i]:
            new_r.append(r1[i])
        else:
            new_r.append("#")
    return "".join(new_r)

def can_move_down():
    global current_rock_locations, chamber
    if 0 in current_rock_locations:  # hittin floor
        return False

    for r, indexes in current_rock_locations.items():
        for i in indexes:
            if r-1 in current_rock_locations and i in current_rock_locations[r-1]:
                # cant collide with other part of rock
                continue
            if chamber[r-1][i] == "#":
                return False
    return True    

def move_rock_down():
    global chamber
    if not can_move_down():
        return False
    
    for r, indexes in current_rock_locations.items():
        for i in indexes:
            new_below = list(chamber[r-1])
            new_below[i] = "#"
            chamber[r-1] = "".join(new_below)
            new_this = list(chamber[r])
            new_this[i] = "."
            chamber[r] = "".join(new_this)
    if not "#" in chamber[-1]:
        chamber.pop()
    move_rock_locations_down()
    return True

def move_rock(dir):
    if dir == "<":
        move_rock_left()
    elif dir == ">":
        move_rock_right()
    else:
        raise Exception("unknown dir %s" % dir)

def print_chamber(s):
    print("%s:" % s)
    for r in reversed(chamber):
        print(r)

def get_o(gases):
    rights = "".join(gases).count(">")
    if rights == 0:
        return DIR_3L
    elif rights == 1:
        return DIR_1L
    elif rights == 2:
        return DIR_1R
    elif rights == 3:
        return DIR_3R
    raise Exception("cant resolve %d right" % rights)

def add_new():
    global current_rock_locations, gas_i
    current_rock_locations = {}
    next_3_gases = [gases[(gas_i + i) % len(gases)] for i in range(0,3)]
    
    gas_i += 3
    o = get_o(next_3_gases)
    rock = rocks[rock_i % len(rocks)]
    rock_post_move = rock.get_post_move(o)

    for row in reversed(rock_post_move):
        chamber.append(row)
        current_rock_locations[len(chamber)-1] = get_indxs(row)

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        gases = l

add_new()   # create starting position of first rock
got_shape = False
shape = None
rocks_stopped = 0

while True:
    if gas_i == len(gases):
        shape = reversed(chamber)
        rocks_stopped = rock_stop_counter
        print("got shape and rocks counter")
        for l in shape: print(l)
        input()

    if gas_i >= len(gases) and rock_stop_counter + rocks_stopped < rock_stop_limit:
        gas_i += len(gases)
        rock_stop_counter += rocks_stopped
        for l in shape:
            chamber.append(l)
        print_chamber("post append")
        continue
    
    print("running manually now")
    gas_dir = gases[gas_i % len(gases)]
    # print_chamber("pre gas")
    move_rock(gas_dir)
    # print_chamber("post gas")

    moved_down = move_rock_down()
    gas_i += 1
    if not moved_down:
        rock_stop_counter += 1
        rock_i += 1
        print(rock_stop_counter)
        if rock_stop_counter >= rock_stop_limit:
            print(get_highest_rock_row()+1)
            exit()
        # print_chamber("pre adding")
        add_new()
        # print_chamber("post adding")
    # input("next round?")
    # print()