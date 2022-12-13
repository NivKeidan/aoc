from queue import PriorityQueue
import regex

class Graph:
    def __init__(self) -> None:
        self.grid = []
        self.visited = []
        self.edges = {}
        self.v = []
    
    def add_row(self, row):
        self.grid.append(row)
    
    def init_v(self):
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                self.v.append(Graph.get_key(r, c))
                
    def make_edges(self):
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                # print("creating edges for node (%d, %d)" % (r, c))

                current_value = self.get_numeric_value(r, c)

                # handle up
                neighborr = r-1
                neighborc = c
                neighbor = self.get_numeric_value(neighborr, neighborc)
                if neighbor != 0 and (neighbor < current_value or neighbor - current_value <= 1):
                    # print("up", current_value, neighbor)
                    self.add_edge(r, c, neighborr, neighborc)
                
                # handle down
                neighborr = r+1
                neighborc = c
                neighbor = self.get_numeric_value(neighborr, neighborc)
                if neighbor != 0 and (neighbor < current_value or neighbor - current_value <= 1):
                    # print("down", current_value, neighbor)
                    self.add_edge(r, c, neighborr, neighborc)

                # handle left
                neighborr = r
                neighborc = c-1
                neighbor = self.get_numeric_value(neighborr, neighborc)
                if neighbor != 0 and (neighbor < current_value or neighbor - current_value <= 1):
                    # print("left", current_value, neighbor)
                    self.add_edge(r, c, neighborr, neighborc)
                
                # handle right
                neighborr = r
                neighborc = c+1
                neighbor = self.get_numeric_value(neighborr, neighborc)
                if neighbor != 0 and (neighbor < current_value or neighbor - current_value <= 1):
                    # print("right", current_value, neighbor)
                    self.add_edge(r, c, neighborr, neighborc)

    
    def get_numeric_value(self, r, c):
        try:
            if r < 0 or c < 0:
                return 0
            letter = self.grid[r][c]
            if letter == 'S':
                letter = 'a'
            if letter == 'E':
                letter = 'z'

            return ord(letter)-96
        except IndexError:
            return 0

    def add_edge(self, origr, origc, tgtr, tgtc):
        # print("creating edges between (%d, %d) and (%d, %d)" % (origr, origc, tgtr, tgtc))
        orig_key = Graph.get_key(origr, origc)
        tgt_key = Graph.get_key(tgtr, tgtc)

        # if orig_key not in self.edges:
        #     self.edges[orig_key] = {}
        # self.edges[orig_key][tgt_key] = 1

        if tgt_key not in self.edges:
            self.edges[tgt_key] = {}
        self.edges[tgt_key][orig_key] = 1

    def get_key(r, c):
        return "%d_%d" % (r, c)
    
    def get_indexes(node_key):
        m = regex.match(r"^(?P<r>[0-9]+)_(?P<c>[0-9]+)$", node_key)
        return m.capturesdict()["r"][0], m.capturesdict()["c"][0]

def dijkstra(graph, startr, startc):
    # D = {v:float('inf') for v in range(graph.v)}
    D = {v:float('inf') for v in graph.v}
    start_vertex = Graph.get_key(startr, startc)
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        # for neighbor in range(graph.v):
        for neighbor in graph.edges[current_vertex]:
            # if graph.edges[current_vertex][neighbor] != -1:
            # we get existing edges allready
            distance = graph.edges[current_vertex][neighbor]
            if neighbor not in graph.visited:
                old_cost = D[neighbor]
                new_cost = D[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    D[neighbor] = new_cost
    return D

def find(ch, s):
    return [i for i, ltr in enumerate(s) if ltr == ch]

possible_starts = []
got_target = False
graph = Graph()

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        graph.add_row(l)

        possible_start_indexes = find('a', l) + find('S', l)
        for j in possible_start_indexes:
            possible_starts.append( (i,j) )

        try:
            targetc = l.index('E')
            targetr = i
            got_target = True
        except ValueError:
            pass

graph.make_edges()
graph.init_v()
target_key = Graph.get_key(targetr, targetc)
res = dijkstra(graph, targetr, targetc)
min = 999999

for k, v in res.items():
    r, c = Graph.get_indexes(k)
    if graph.get_numeric_value(int(r), int(c)) == 1:
        if v <= min:
            min = v
            print(k, v)
print(min)

# min = 99999999
# for s in possible_starts:
#     graph.visited = []
#     res = dijkstra(graph, s[0], s[1])
#     if res[target_key] < min:
#         min = res[target_key]
#         print(min)

# print(min)