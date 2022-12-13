stacks = []
stack_num = 0
reading_stacks = True

import regex

def show_stacks():
    global stack_num
    for j in range(stack_num):
        print("%d: %s" % (j, stacks[j]))

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        if l.startswith(" 1   2"):
            reading_stacks = False
            for j in range(stack_num):
                stacks[j].reverse()
            show_stacks()
            continue
        if l == "":
            continue

        if reading_stacks:
            if i == 0:
                stack_num = int((len(l)+1) / 4)
                print("total stacks are", stack_num)
                for j in range(stack_num):
                    stacks.append([])

            for j in range(stack_num):
                c = l[j*4+1]
                if c == " ":
                    continue
                stacks[j].append(c)
        else:
            m = regex.match(r"^move (?P<num>[0-9]+) from (?P<from>[0-9]+) to (?P<to>[0-9]+)$", l)
            if m is None:
                continue
            origin = int(m.capturesdict()["from"][0])
            num = int(m.capturesdict()["num"][0])
            destination = int(m.capturesdict()["to"][0])

            moves = stacks[origin-1][-1*num:]
            print("moving", moves)
            # moves.reverse()
            stacks[destination-1] = stacks[destination-1] + moves
            stacks[origin-1] = stacks[origin-1][:-1*num]
            show_stacks()

for j in range(stack_num):
    print(stacks[j][-1], end="")
print()