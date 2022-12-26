import regex
no_beacons = {}
debug_row = 99999999999

def get_man_dist(xa, ya, xb, yb):
    return abs(xb - xa) + abs(yb - ya)

def add_block(y, minx, maxx):
    if y == debug_row:
        debug = True
    else:
        debug = False
    
    if debug: print("adding block %d->%d in row %d" % (minx, maxx, y))
    if y not in no_beacons:
        no_beacons[y] = []


    for i, block in enumerate(no_beacons[y]):
        blockmin = block[0]
        blockmax = block[1]

        if debug: print("chcekng for block (%d, %d)" % (blockmin, blockmax))
        # starts before
            # ends before - add before current index, finish
            # ends start of new - change current to start, finish
            # ends in middle - change current to start, finish
            # end end of new - change current to start, finish
            # ends after - remove this, re-run function
        # starts same:
            # ends in start - do nothing, finish
            # ends in middle - do nothin, finish
            # ends with end - do nothing, finish
            # ends after - remove current, re run function
        # starts middle:
            # ends middle - do nothing, finish
            # ends with end - do nothing, finish
            # ends after - change min to start of block, remove block, re run function
        # starts end:
            # end end - do nothing, finish
            # ends after - update min, remove this, re run function
        # starts after - continue to next
        # if ended, so append

        if minx < blockmin:
            if debug: print("starts before")
            if maxx < blockmin:
                if debug: print("ends before. adding")
                no_beacons[y] = no_beacons[y][:i] + [(minx, maxx)] + no_beacons[y][i:]
                if debug: print(no_beacons[y])
                return
            if maxx > blockmax:
                if debug: print("ends after")
                no_beacons[y] = no_beacons[y][:i] + no_beacons[y][i+1:]
                if debug: print(no_beacons[y])
                return add_block(y, minx, maxx)
            if debug: print("ends in start/middle/end")
            no_beacons[y][i] = (minx, blockmax)
            if debug: print(no_beacons[y])
            return
        if minx == blockmin:
            if debug: print("starts same")
            if maxx > blockmax:
                if debug: print("ends after")
                no_beacons[y] = no_beacons[y][:i] + no_beacons[y][i+1:]
                if debug: print(no_beacons[y])
                return add_block(y, minx, maxx)
            return
        if minx < blockmax:
            if debug: print("starts middle")
            if maxx > blockmax:
                if debug: print("ends after")
                minx = blockmin
                no_beacons[y] = no_beacons[y][:i] + no_beacons[y][i+1:]
                if debug: print(no_beacons[y])
                return add_block(y, minx, maxx)
            return
        if minx == blockmax:
            if debug: print("starts at end")
            if maxx > blockmax:
                if debug: print("ends after")
                minx = blockmin
                no_beacons[y] = no_beacons[y][:i] + no_beacons[y][i+1:]
                if debug: print(no_beacons[y])
                return add_block(y, minx, maxx)
    if debug: print("appending to end of list")
    no_beacons[y].append((minx, maxx))
    if debug: print(no_beacons[y])

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        m = regex.match(r"^Sensor at x=(?P<sx>[-0-9]+), y=(?P<sy>[-0-9]+): closest beacon is at x=(?P<bx>[-0-9]+), y=(?P<by>[-0-9]+)$", l)
        if m is not None:
            sx = int(m.capturesdict()["sx"][0])
            sy = int(m.capturesdict()["sy"][0])
            bx = int(m.capturesdict()["bx"][0])
            by = int(m.capturesdict()["by"][0])
            add_block(by, bx, bx)
            man_dist = get_man_dist(sx, sy, bx, by)
            for j in range(0, man_dist):
                minx = sx - (man_dist - j)
                maxx = sx + (man_dist -j)
                add_block(sy-j, minx, maxx)
                add_block(sy+j, minx, maxx)

for y in range(4000000):
    if len(no_beacons[y]) > 1:
        print(y, no_beacons[y])