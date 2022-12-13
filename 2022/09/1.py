class Knot:
    x = 0
    y = 0
    
knots_num = 10

locations = []
for i in range(knots_num):
    locations.append(Knot())

tail_spots = {0: {0: True}}

def move_knots():
    for i in range(1, len(locations)):
        if should_knot_move(i):
            move_knot(i)

def should_knot_move(i):
    prev = locations[i-1]
    curr = locations[i]
    hx, hy = prev.x, prev.y
    tx, ty = curr.x, curr.y
    
    if hx == tx or hy == ty:
        return abs(hx - tx) + abs(hy - ty) >= 2
    else:
        return abs(hx - tx) + abs(hy - ty) > 2

def move_knot(i):
    prev = locations[i-1]
    curr = locations[i]
    hx, hy = prev.x, prev.y
    tx, ty = curr.x, curr.y

    if hy > ty:
        curr.y += 1
    elif hy < ty:
        curr.y -= 1
    if hx > tx:
        curr.x += 1
    elif hx < tx:
        curr.x -= 1
    if i == 9:
        save_spot(curr.x, curr.y)

def save_spot(x, y):
    global tail_spots
    if x not in tail_spots:
        tail_spots[x] = {}
    tail_spots[x][y] = True

def print_knots():
    for k in locations:
        print("(%d, %d)" % (k.x, k.y), end=",")
    print()

def move_head(dir):
    if dir == "R":
        locations[0].x += 1
    elif dir == "U":
        locations[0].y += 1
    elif dir == "D":
        locations[0].y -= 1
    elif dir == "L":
        locations[0].x -= 1
    move_knots()

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        dir = l[0]
        cnt = int(l[2:])
        for j in range(cnt):
            move_head(dir)
        print("moving %d %s" % (cnt, dir))
        print_knots()

cnt = 0
for v in tail_spots.values():
    cnt += len(v.keys())
print(cnt)
# print(tail_spots)