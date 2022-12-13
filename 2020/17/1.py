actives = {}  # z, x, y
turn_num = 0
start_size=8
cycles = 6

def add_to_actives(acts, z, w, x, y):
    if z not in acts:
        acts[z] = {}
    if w not in acts[z]:
        acts[z][w] = {}
    if x not in acts[z][w]:
        acts[z][w][x] = {}
    if y not in acts[z][w][x]:
        acts[z][w][x][y] = {}
    acts[z][w][x][y] = True

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        for j, c in enumerate(l):
            if c =="#":
                add_to_actives(actives, 0, 0, i, j)

def count_active_neighbors(z, w, x, y):
    options = [(-1, -1, -1, -1), (-1, 0, -1, -1), (-1, 1, -1, -1), (-1, -1, -1, 0), (-1, 0, -1, 0), (-1, 1, -1, 0), (-1, -1, -1, 1), (-1, 0, -1, 1), (-1, 1, -1, 1), (-1, -1, 0, -1), (-1, 0, 0, -1), (-1, 1, 0, -1), (-1, -1, 0, 0), (-1, 0, 0, 0), (-1, 1, 0, 0), (-1, -1, 0, 1), (-1, 0, 0, 1), (-1, 1, 0, 1), (-1, -1, 1, -1), (-1, 0, 1, -1), (-1, 1, 1, -1), (-1, -1, 1, 0), (-1, 0, 1, 0), (-1, 1, 1, 0), (-1, -1, 1, 1), (-1, 0, 1, 1), (-1, 1, 1, 1), (0, -1, -1, -1), (0, 0, -1, -1), (0, 1, -1, -1), (0, -1, -1, 0), (0, 0, -1, 0), (0, 1, -1, 0), (0, -1, -1, 1), (0, 0, -1, 1), (0, 1, -1, 1), (0, -1, 0, -1), (0, 0, 0, -1), (0, 1, 0, -1), (0, -1, 0, 1), (0, 0, 0, 1), (0, 1, 0, 1), (0, -1, 1, -1), (0, 0, 1, -1), (0, 1, 1, -1), (0, -1, 1, 0), (0, 0, 1, 0), (0, 1, 1, 0), (0, -1, 1, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, -1, -1, -1), (1, 0, -1, -1), (1, 1, -1, -1), (1, -1, -1, 0), (1, 0, -1, 0), (1, 1, -1, 0), (1, -1, -1, 1), (1, 0, -1, 1), (1, 1, -1, 1), (1, -1, 0, -1), (1, 0, 0, -1), (1, 1, 0, -1), (1, -1, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0), (1, -1, 0, 1), (1, 0, 0, 1), (1, 1, 0, 1), (1, -1, 1, -1), (1, 0, 1, -1), (1, 1, 1, -1), (1, -1, 1, 0), (1, 0, 1, 0), (1, 1, 1, 0), (1, -1, 1, 1), (1, 0, 1, 1), (1, 1, 1, 1), (0, -1, 0, 0), (0, 1, 0, 0)]

    c = 0
    for opt in options:
        try:
            if actives[z+opt[0]][w+opt[1]][x+opt[2]][y+opt[3]]:
                c += 1
        except KeyError:
            continue
    return c

def is_active(z, w, x, y):
    try:
        if actives[z][w][x][y]:
            return True
    except KeyError:
        return False

def get_layers():
    layers = [0]
    turns = turn_num
    while turns > 0:
        first = layers[0]
        last = layers[-1]
        layers.append(last+1)
        layers = [first - 1] + layers
        turns -= 1
    return layers

def get_size():
    base = list(range(start_size))
    turns = turn_num
    while turns > 0:
        first = base[0]
        last = base[-1]
        base.append(last+1)
        base = [first - 1] + base
        turns -= 1
    return base

def next_actives():
    global actives, turn_num
    next_actives = {}
    turn_num += 1

    for z in get_layers():
        for w in get_layers():
            for x in get_size():
                for y in get_size():
                    
                    active_neighbors = count_active_neighbors(z, w, x, y)
                    is_act = is_active(z, w, x, y)
                    # print("checking", z, w, x, y, is_act, active_neighbors)
                    if is_act and active_neighbors in [2,3]:
                        add_to_actives(next_actives, z, w, x, y)
                    elif not is_act and active_neighbors == 3:
                        add_to_actives(next_actives, z, w, x, y)

    actives = next_actives
    

def print_actives():
    print("actives:", end="")
    for z in actives.keys():
        for w in actives[z].keys():
            for x in actives[z][w].keys():
                for y in actives[z][w][x].keys():
                    print(z, w, x, y, end=", ")
    print()

for i in range(cycles):
    # print_actives()
    # input()
    next_actives()

c = 0
for z in actives.keys():
    for w in actives[z].keys():
        for x in actives[z][w].keys():
            for y in actives[z][w][x].keys():
                c += 1
print(c)