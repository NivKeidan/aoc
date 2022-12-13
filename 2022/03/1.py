total_priorities = 0
groups = []
possible_group_chars = {}

def get_score(c):
    ascii_code = ord(c)
    if ascii_code > 96:  # small letters
        return ascii_code - 96
    return ascii_code - 38

with open('inp1') as f:
    inner_group = 0
    current_group = []

    for i, l in enumerate(f.readlines()):
        l = l.strip()
        inner_group += 1
        if inner_group > 3:
            # new group starting
            groups.append(current_group)
            current_group = []
            inner_group = 1
        current_group.append(l)
    groups.append(current_group)
    current_group = []
    inner_group = 1

for i, group in enumerate(groups):
    group_tracker = {}
    for elf in group:
        counted = {}
        for c in elf:
            if c in counted:
                continue
            counted[c] = True

            if c in group_tracker:
                group_tracker[c] += 1
            else:
                group_tracker[c] = 0
    all_options = []
    for k, v in group_tracker.items():
        if v == 2:
            all_options.append(k)
    possible_group_chars[i] = all_options

tot = 0
for k, v in possible_group_chars.items():
    tot += get_score(v[0])
print(tot)