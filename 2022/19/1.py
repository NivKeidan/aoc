import regex, queue

class Blueprint:
    def __init__(self, i, cost_ore, cost_clay, cost_obs, cost_geode) -> None:
        self.costs = {
            ORE: cost_ore,
            CLAY: cost_clay,
            OBS: cost_obs,
            GEODE: cost_geode
        }
        self.index = i
    
    def __repr__(self) -> str:
        return "bp %d: ore robot costs %s, clay robot costs %s, obs robot costs %s, geode robot costs %s" % (self.index, self.costs[ORE], self.costs[CLAY], self.costs[OBS], self.costs[GEODE])

GEODE = "RGE"
OBS = "ROBS"
CLAY = "RCLAY"
ORE = "RORE"
robot_types_order = [GEODE, OBS, CLAY, ORE]
max_turns = 32

bps = []

def next_turn_res(robots, res, turns=1):
    cres = res.copy()
    for _ in range(turns):
        for rt, ra in robots.items():
            cres[rt] += ra
    return cres

def reduce_cost(bp, t, res):
    cres = res.copy()
    for t, a in bp.costs[t].items():
        cres[t] -= a
    return cres

def can_build(bp, t, res):
    for cost_type, cost_amount in bp.costs[t].items():
        if cost_amount > res[cost_type]:
            return False
    return True

def has_robot(robots,t):
    for r in robots:
        if r.t == t:
            return True
    return False

def get_turns_to_build(bp, robots, res, t):
    cres = res.copy()
    c = 0
    costs = bp.costs[t]
    for ct in costs.keys():
        if robots[ct] == 0:    # can not build at all
            return -1
    while not can_build(bp, t, cres):
        cres = next_turn_res(robots, cres, 1)
        c += 1
    return c

def add_robot(robots, t):
    crobots = robots.copy()
    crobots[t] += 1
    return crobots

# populate blueprints
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        m = regex.match(r"^Blueprint [0-9]+: Each ore robot costs (?P<ore_robot_cost>[0-9]+) ore. Each clay robot costs (?P<clay_robot_cost>[0-9]+) ore. Each obsidian robot costs (?P<obs_robot_cost_ore>[0-9]+) ore and (?P<obs_robot_cost_clay>[0-9]+) clay. Each geode robot costs (?P<geode_robot_cost_ore>[0-9]+) ore and (?P<geode_robot_cost_obs>[0-9]+) obsidian.$", l)
        if m is None:
            raise Exception("failed regex: %s" % l)
        
        ore_robot_cost = int(m.capturesdict()["ore_robot_cost"][0])
        clay_robot_cost = int(m.capturesdict()["clay_robot_cost"][0])
        obs_robot_cost_ore = int(m.capturesdict()["obs_robot_cost_ore"][0])
        obs_robot_cost_clay = int(m.capturesdict()["obs_robot_cost_clay"][0])
        geode_robot_cost_ore = int(m.capturesdict()["geode_robot_cost_ore"][0])
        geode_robot_cost_obs = int(m.capturesdict()["geode_robot_cost_obs"][0])
        bp = Blueprint(i,
            {ORE: ore_robot_cost},
            {ORE: clay_robot_cost},
            {ORE: obs_robot_cost_ore, CLAY: obs_robot_cost_clay},
            {ORE: geode_robot_cost_ore, OBS: geode_robot_cost_obs},
        )
        bps.append(bp)

def do(bp, ind):
    starting_res = {
        ORE: 0,
        CLAY: 0,
        OBS: 0,
        GEODE: 0
    }
    starting_robots = {
        ORE: 1,
        CLAY: 0,
        OBS: 0,
        GEODE: 0
    }
    maxes= {
        ORE: max([c[ORE] for t, c in bp.costs.items() if ORE in c]),
        CLAY: max([c[CLAY] for t, c in bp.costs.items() if CLAY in c]),
        OBS: max([c[OBS] for t, c in bp.costs.items() if OBS in c]),
    }

    q = queue.Queue()
    q.put((0, starting_robots, starting_res))
    m = 0

    while not q.empty():
        state = q.get()
        turn = state[0]
        robots = state[1]
        res = state[2]

        for robot_type in robot_types_order:
            if robot_type != GEODE and robots[robot_type] >= maxes[robot_type]:
                continue
            turns_to_build = get_turns_to_build(bp, robots, res, robot_type)
            if turns_to_build < 0:
                continue
            new_turn = turn + turns_to_build + 1
            if new_turn > max_turns:
                continue
            new_res = reduce_cost(bp, robot_type, next_turn_res(robots, res, turns_to_build+1))
            new_robots = add_robot(robots, robot_type)
            q.put( (new_turn, new_robots, new_res))
        cnt = res[GEODE] + (max_turns - turn) * robots[GEODE]
        
        if cnt > m:
            m = cnt
    print("%d: %d" % (ind, m))
    return m

for i, bp in enumerate(bps):
    print("running %d" % i)
    f = do(bp, i)