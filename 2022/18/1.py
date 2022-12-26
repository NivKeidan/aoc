def get_op(s):
    if s == "left":
        return "right"
    if s == "right":
        return "left"
    if s == "top":
        return "bot"
    if s == "bot":
        return "top"
    if s == "front":
        return "back"
    if s == "back":
        return "front"
    raise Exception("no such side %s" % s)

class Cube:
    def __init__(self, x, y, z, air=False) -> None:
        self.size = 1
        self.x = x
        self.y = y
        self.z = z
        self.air = air
        self.checked = {"left": False, "right": False, "top": False, "bot": False, "front": False, "back": False}
        self.reach_out = False

    def __repr__(self) -> str:
        return "C[%d, %d, %d]" % (self.x, self.y, self.z)
    
    def get_air_neighbors(self):
        neighbors = []
        for adj in [self.get_adj_cube("left"), self.get_adj_cube("right"), self.get_adj_cube("top"), self.get_adj_cube("bot"), self.get_adj_cube("front"), self.get_adj_cube("back")]:
            if adj is not None and adj.is_air():
                neighbors.append(adj)
        return neighbors

    
    def get_adj_cube(self, s):
        x = self.x
        y = self.y
        z = self.z

        if s == "left":
            x -= 1
        if s == "right":
            x += 1
        if s == "top":
            y += 1
        if s == "bot":
            y -= 1
        if s == "front":
            z -= 1
        if s == "back":
            z += 1
        try:
            return grid[x][y][z]
        except KeyError:
            return None
    
    def mark_checked(self, s):
        self.checked[s] = True
    
    def is_air(self):
        return self.air
    
    def mark_reachable(self):
        self.reach_out = True

    def check_all_sides(self):
        cnt = 0
        for side, checked in self.checked.items():
            if not checked:
                self.mark_checked(side)
                c = self.get_adj_cube(side)
                if c is None:
                    cnt += 1  # at the edge of grid
                    continue
                c.mark_checked(get_op(side))
                if c.is_air() and c.reach_out:
                    cnt += 1
        return cnt

grid_size = 20
grid = {}

for x in range(grid_size):
    grid[x] = {}
    for y in range(grid_size):
        grid[x][y] = {}
        for z in range(grid_size):
            grid[x][y][z] = Cube(x, y, z, True)

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        [sx, sy, sz] = [int(x) for x in l.split(",")]
        c = Cube(sx, sy, sz, False)
        grid[sx][sy][sz] = c

def mark_neighbor_airs_reachable(c, visited=set()):
    # print("getting: %s, visited: %s" % (c, visited))
    visited.add(c)
    for neighbor in c.get_air_neighbors():
        if neighbor in visited or neighbor.reach_out:
            continue
        # print("marking %s reachable" % neighbor)
        neighbor.mark_reachable()
        mark_neighbor_airs_reachable(neighbor, visited)

reachables = set()
for i in range(grid_size):
    for j in range(grid_size):
        cx = grid[0][i][j]
        cy = grid[i][0][j]
        cz = grid[i][j][0]
        for c in [cx, cy, cz]:
            if c.is_air():
                c.mark_reachable()
                reachables.add(c)

import sys
# input(sys.getrecursionlimit())
sys.setrecursionlimit(3500)


for rc in reachables:
    mark_neighbor_airs_reachable(rc, set())

cnt = 0
for x in grid:
    for y in grid[x]:
        for z in grid[x][y]:
            c = grid[x][y][z]
            if not c.is_air():
                cnt += c.check_all_sides()
print(cnt)