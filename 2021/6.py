import sys

file_name = "./6/test"
const_cycle = 6
new_fish_cycle= 8
day_num = int(sys.argv[1])
ind = 0

class Fish:
    def __init__(self, d, p=None) -> None:
        global ind
        self.cnt = d
        self.id = ind
        ind += 1
        self.parent = p
        self.calced = False
        # print("new fish - %s [%s]" % (self.id, self.parent.id if self.parent is not None else ""))
    
    def __repr__(self) -> str:
        return str(self.cnt)
    
    def get_name(self) -> str:
        s = "%d" % self.id
        if self.parent is not None:
            s += "["
            f = self
            while f.parent is not None:
                s += "%d," % f.parent.id
                f = f.parent
            s = s[:-1]+"]"
        return s

    def getCountWithOffsprings(self, days_left):
        # print()
        # print("fish %d, countdown %s, days left %d" % (self.id, self.cnt, days_left))
        if days_left == 0 or days_left <= self.cnt:
            # print("fish %s returning 1" % self.get_name())
            return 1

        # first fish after 8 (or less) days
        days_left -= self.cnt + 1
        # print("%d spawning new fish, days left %d" % (self.id, days_left))
        new_fish = Fish(new_fish_cycle, self)
        count = new_fish.getCountWithOffsprings(days_left)
        
        # rest of spawns
        while days_left > const_cycle:
            days_left -= const_cycle+1
            # print("%d spawning new fish, days left %d" % (self.id, days_left))
            new_fish = Fish(new_fish_cycle, self)
            count += new_fish.getCountWithOffsprings(days_left)
            
        self.calced = True
        count += 1
        print("fish %s returning %d" % (self.get_name(), count))
        # input()
        return count
    
fishes = []

with open(file_name) as f:
    for l in f.readlines():
        l = l.strip()

        for d in l.split(","): 
            fishes.append(Fish(int(d)))
    
counter = 0
for f in fishes:
    counter += f.getCountWithOffsprings(day_num)

print(counter)

