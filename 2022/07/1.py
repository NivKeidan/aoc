import regex

def add_to_map_int(m, i, v):
    if i not in m:
        m[i] = v
    else:
        m[i] += v

class Node:
    def __init__(self, n):
        self.name = n
        self.parent = None
    
    def __str__(self):
        if self.name == "":
            return "root"
        return self.name

    def get_full_path(self):
        if self.parent is None:
            return self.name
        return self.parent.get_full_path() + "/" + str(self)

class Dir(Node):
    def __init__(self, n):
        super().__init__(n)
        self.is_dir = True
        self.size = 0
        self.children = []

    def find_child_by_name(self, n):
        for c in self.children:
            if c.name == n:
                return c
        return None

    def add_child(self, n):
        for c in self.children:
            if c.name == n:
                return  # dont add twice
        n.parent = self
        self.children.append(n)

    def get_size(self):
        if self.size <= 0:
            sum = 0
            for c in self.children:
                sum += c.get_size()
            self.size = sum
        return self.size

class File(Node):
    def __init__(self, n, s):
        super().__init__(n)
        self.is_dir = False
        self.size = s

    def get_size(self):
        return self.size

root = Dir("")
current_dir = [root]

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        # ls command
        if l == "$ ls":
            continue
        
        # cd command
        m = regex.match(r"^\$ cd (?P<dir_name>.*)$", l)
        if m is not None:
            target = m.capturesdict()["dir_name"][0]
            if target == "..":
                current_dir = current_dir[:-1]
                # next_dir = current_dir[-1].parent
            else:
                next_dir = current_dir[-1].find_child_by_name(target)
                if next_dir is None:
                    raise Exception("dir %s does not exist in %s" % (target, current_dir[-1]))
                current_dir.append(next_dir)
            print("cwd", current_dir[-1])
            continue
        
        # ls output - dir
        m = regex.match(r"^dir (?P<containerd_dir_name>.*)$", l)
        if m is not None:
            d = m.capturesdict()["containerd_dir_name"][0]
            print("dir %s in dir %s" % (d, current_dir[-1]))
            new_dir = Dir(d)
            current_dir[-1].add_child(new_dir)
            continue
        
        # ls output - file size
        m = regex.match(r"^(?P<size>[0-9]+) (?P<file_name>.*)$", l)
        if m is not None:
            s = int(m.capturesdict()["size"][0])
            n = m.capturesdict()["file_name"][0]
            print("file %s(%d) in dir %s" % (n, s, current_dir[-1]))
            f = File(n, s)
            current_dir[-1].add_child(f)
            continue

sums = {}
def store_sizes(n):
    if n.is_dir:
        sums[n.get_full_path()] = n.get_size()
    for c in n.children:
        if c.is_dir:
            store_sizes(c)

store_sizes(root)

total = 70000000
used = root.get_size()
free = total - used
target = 30000000
required_space = target - free

print("total: %d, used: %d, free: %d, target: %d, missing: %d" % (total, used, free, target, required_space))
current_d = None
current_s = None

for d, s in sums.items():
    if s >= required_space:
        if current_s is None:
            current_d = d
            current_s = s
        else:
            if s < current_s:
                current_s = s
                current_d = d
print(current_d, current_s)