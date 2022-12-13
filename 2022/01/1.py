elves = []
current_sum = 0

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        if l == "":
            elves.append(current_sum)
            current_sum = 0
            continue
            
        current_sum += int(l)

# handle last elf
elves.append(current_sum)
current_sum = 0

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])