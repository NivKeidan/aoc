import regex
cycle = 0
sprite_middle = 1

drawing = []

def next_cycle():
    global next_str, cycle
    draw()
    cycle += 1

def draw():
    if abs(sprite_middle - (cycle % 40)) <= 1:
        drawing.append("#")
    else:
        drawing.append(".")

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        print("cycle %d reg %d" % (cycle, sprite_middle))
        m = regex.match(r"^addx (?P<val>.*)$", l)
        next_cycle()
        if m is not None:
            val = int(m.capturesdict()["val"][0])
            next_cycle()
            sprite_middle += val

    for i in range(2):  # run 2 more cycles
        print("cycle %d, reg %d" % (cycle, sprite_middle))
        cycle += 1

for i, v in enumerate(drawing):
    if i % 40 == 0:
        print()
    print(v, end="")
print()