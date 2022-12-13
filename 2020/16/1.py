import regex

# rule_num = 3
rule_num = 20
max_num = 999
a = [False] * max_num
by_name = {}


possible_rules_by_name = {}
possible_rules_by_index = {}
for i in range(0, rule_num):
    possible_rules_by_index[i] = []

nownow = False
valid_tickets = []

finals = {}

   
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if i < rule_num:
            m = regex.match(r"^(?P<field_name>[\w ]+): (?P<r1_min>[0-9]+)-(?P<r1_max>[0-9]+) or (?P<r2_min>[0-9]+)-(?P<r2_max>[0-9]+)$", l)
            if m is None:
                raise Exception("bad regex")
            field_name = m.capturesdict()["field_name"][0]
            r1_min = int(m.capturesdict()["r1_min"][0])
            r1_max = int(m.capturesdict()["r1_max"][0])
            r2_min = int(m.capturesdict()["r2_min"][0])
            r2_max = int(m.capturesdict()["r2_max"][0])
            possible_rules_by_name[field_name] = []
            
            t = [False] * max_num
            for i in range(r1_min-1, r1_max):
                t[i] = True
                a[i] = True
            
            for i in range(r2_min-1, r2_max):
                t[i] = True
                a[i] = True
            
            by_name[field_name] = t
        else:
            if l == "nearby tickets:":
                nownow = True
                continue
            if nownow:
                nums = [int(x) for x in l.split(",")]
                valid_tickets.append(nums)
                for n in nums:
                    if a[n-1] is False:
                        del valid_tickets[-1]
                        break

def populate_possbiles():
    global possible_rules_by_name, possible_rules_by_index
    for k in possible_rules_by_index.keys():
        possible_rules_by_index[k] = []
    for k in possible_rules_by_name.keys():
        possible_rules_by_name[k] = []

    for rule, rule_range in by_name.items():
        for i in range(0, rule_num):
            for ticket in valid_tickets:
                # if rule == "class": print(ticket); print(rule_range[:10]); print(ticket[i]); print(rule_range[ticket[i]])
                if rule_range[ticket[i]-1] is False:
                    this_is_it = False
                    break
                else:
                    this_is_it = True
            if this_is_it:
                possible_rules_by_name[rule].append(i)
                possible_rules_by_index[i].append(rule)

def remove_from_dicts(rule, index):
    del possible_rules_by_name[rule]
    del possible_rules_by_index[index]

    for ops in possible_rules_by_name.values():
        try:
            ops.remove(index)
        except ValueError:
            continue
    
    for ops in possible_rules_by_index.values():
        try:
            ops.remove(rule)
        except ValueError:
            continue

def print_less_than(i):
    for ind, rule_opts in possible_rules_by_index.items():
        if len(rule_opts) <= i:
            print(ind, rule_opts)
    print()
    for rule, ind_opts in possible_rules_by_name.items():
        if len(ind_opts) <= i:
            print(rule, ind_opts)

populate_possbiles()
print(possible_rules_by_index)
print(possible_rules_by_name)
while True:
    to_remove = None

    for rule, options in possible_rules_by_name.items():
        if len(options) == 1:
            print("rule %s is at index %d" % (rule, options[0]))
            to_remove = (rule, options[0])
            break
    
    if to_remove is None:
        for ind, rule_opts in possible_rules_by_index.items():
            if len(rule_opts) == 1:
                print("index %d is rule %s" % (ind, rule_opts[0]))
                to_remove = (rule_opts[0], ind)
                break
    
    if to_remove is not None:
        remove_from_dicts(to_remove[0], to_remove[1])
        continue
    else:
        exit()