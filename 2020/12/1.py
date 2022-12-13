locations = {
    "ship": {"east": 0, "north": 0},
    "wp": {"east": 10, "north": 1}
}

def rotate(d, n):
    while n > 0:
        current_q, diff_e, diff_n = get_current_quarter()
        current_e = locations["wp"]["east"]
        current_n = locations["wp"]["north"]
        new_e = current_e
        new_n = current_n

        # ship (10, 5), diff: (10, -1), wp (20, 4) -> wp (9, -5), diff: (-1, -10)
        # to calculate, set diff according to required quarter
        # then set wp according to diff and ship
        # then set desired new diff
        # then set new wp
        # then extract formulas

        
        # q1/L:
        #     new_e = old_e - (diffe + diffn)
        #     new_n = old_n + (diffe - diffn)
        # q2/L:
        #     new_e = old_e - (diffe - diffn)
        #     new_n = old_n + (diffe - diffn)
        # q3/L:
        #     new_e = old_e - (diffe + diffn)
        #     new_n = old_n + (diffe - diffn)
        # q4/L:
        #     new_e = old_e - (diffe + diffn)
        #     new_n = old_n - (diffe - diffn)
        
        # q1/R:
        #     new_e = old_e - (diffe - diffn)
        #     new_n = old_n - (diffe + diffn)
        # q2/R:
        #     new_e = old_e - (diffe - diffn)
        #     new_n = old_n - (diffe + diffn)
        # q3/R:
        #     new_e = old_e - (diffe - diffn)
        #     new_n = old_n - (diffe + diffn)
        # q4/R:
        #     new_e = old_e - (diffe - diffn)
        #     new_n = old_n - (diffe + diffn)

        if d == "R":
            new_e = current_e - diff_e + diff_n
            new_n = current_n - diff_e - diff_n
        elif d == "L":
            new_e = current_e - diff_e - diff_n
            new_n = current_n + diff_e - diff_n
        else:
            raise Exception("current quarter is", current_q)

        set_loc("wp", "east", new_e)
        set_loc("wp", "north", new_n)
        n -= 90

def get_diffs():
    return locations["wp"]["east"] - locations["ship"]["east"], locations["wp"]["north"] - locations["ship"]["north"]

def get_current_quarter():
    diff_e, diff_n = get_diffs()
    if diff_e >= 0 and diff_n >= 0:
        q = 1
    elif diff_e <= 0 and diff_n >= 0:
        q = 2
    elif diff_e <= 0 and diff_n <= 0:
        q = 3
    elif diff_e >= 0 and diff_n <= 0:
        q = 4
    else:
        raise Exception("cant figure out quarter")
    
    return q, diff_e, diff_n

def set_loc(o, d, n):
    locations[o][d] = n

def move(o, d, n):
    global locations
    if d == "E":
        locations[o]["east"] += n
    elif d == "W":
        locations[o]["east"] -= n
    elif d == "N":
        locations[o]["north"] += n
    elif d == "S":
        locations[o]["north"] -= n
    else:
        raise Exception("unknown dircetion", d)

def print_all():
    print("ship at (%d,%d), wp at (%d,%d)" % (locations["ship"]["east"], locations["ship"]["north"], locations["wp"]["east"], locations["wp"]["north"]))
    print("wp relative to ship: (%d, %d)" % get_diffs())

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        direction = str(l[0])
        count = int(l[1:])
        print_all()
        # input("input: %s" % l)
        print("input: %s" % l)

        if direction in ["R", "L"]:
            rotate(direction, count)
        elif direction == "F":
            diff_e, diff_n = get_diffs()
            move_east = diff_e * count
            move_north = diff_n * count
            locations["ship"]["east"] += move_east
            locations["ship"]["north"] += move_north
            locations["wp"]["north"] += move_north
            locations["wp"]["east"] += move_east
        else:
            move("wp", direction, count)
        
print_all()
print(abs(locations["ship"]["east"]) +  abs(locations["ship"]["north"]))
