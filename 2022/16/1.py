import regex, itertools
flows = {}
paths = {}
openable_valves = []

def shortest_route(tgt, visited=set(), rte=[]):
    # from va to vb
    va = rte[-1]
    # print("finding route %s -> %s" %(rte, tgt))

    if tgt in paths[va]:
        return 1, rte + [tgt]

    shortest = 999
    shortest_rt = None
    for pv in paths[va]:
        crt = rte  + [pv]
        cvstd = visited.copy()
        # print("checking", pv, crt, visited, rte)
        if pv in cvstd:
            continue
        cvstd.add(pv)
        sr, new_rt = shortest_route(tgt, cvstd, crt)
        if sr == 999:
            continue
        if sr+1 < shortest:
            shortest = sr + 1
            shortest_rt = new_rt
    return shortest, shortest_rt
        
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        m = regex.match(r"^Valve (?P<valve>[A-Z]+) has flow rate=(?P<flow>[0-9]+); tunnel[s]? lead[s]? to valve[s]? (?P<paths>[A-Z, ]+)$", l)
        if m is not None:
            v = m.capturesdict()["valve"][0]
            flow = int(m.capturesdict()["flow"][0])
            flows[v] = flow
            if flow > 0:
                openable_valves.append(v)
            paths[v] = m.capturesdict()["paths"][0].split(", ")

valves_to_check = set(openable_valves + ['AA'])
shortests = {}
for v in valves_to_check:
    for v2 in valves_to_check:
        if v == v2:
            continue
        t, _ = shortest_route(v2, set(), [v])
        if v not in shortests:
            shortests[v] = {}
        shortests[v][v2] = t

def move_turns(i):
    global time, pres_out
    for _ in range(i):
        time += 1
        # print("adding %d" % pres_per_turn)
        pres_out += pres_per_turn

time = 0
pres_out = 0
pres_per_turn = 0
current_valve = 'AA'

max = 0
finalr = None
for rte in itertools.permutations(openable_valves):
    # print(rte)
    time = 0
    pres_out = 0
    pres_per_turn = 0
    current_valve = 'AA'
    
    for i in range(len(rte)):
        turns_ahead, pres_addon, per_turn_addon = get_res(rte[i:])
        if turns_ahead > 0:
            time += turns_ahead
            pres_out += pres_addon
            pres_per_turn += per_turn_addon
            if i > 0:
                store_new_result(rte[i-1:], turns_ahead)
            break

    for v in rte:
        # walk to valve
        # turns_walking, route = shortest_route(v, set([current_valve]), [current_valve])
        turns_walking = shortests[current_valve][v]
        # print("walking from %s to %s (%d) %s" %(current_valve, v, time, route))
        move_turns(turns_walking)
        current_valve = v

        # open valve
        # print("opening valve %s (%d)" % (v, time))
        move_turns(1)
        pres_per_turn += flows[v]
    for i in range(time, 30):
        move_turns(1)
    print("total pres %d for rte %s" % (pres_out, rte))
    if pres_out > max:
        finalr = rte
        max = pres_out
print(max, finalr)