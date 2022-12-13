hor = 0
dep = 0
FOR = "forward"
DWN = "down"
UP = "up"

aim = 0

with open('./2/inp') as f:
    for l in f.readlines():
        action, val = l.split(" ")
        if action == FOR:
            hor += int(val)
            dep += int(val)*aim
        elif action == DWN:
            aim += int(val)
        elif action == UP:
            aim -= int(val)
print("hor: %s, dep: %s, final: %s" % (hor, dep, hor*dep))