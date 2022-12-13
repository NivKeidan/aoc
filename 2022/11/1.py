def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

class Item:
    def __init__(self, wl) -> None:
        self.wl = wl
        self.multis = {}
        self.addon = 0
        for f in prime_factors(wl):
            if f not in self.multis:
                self.multis[f] = 0
            self.multis[f] += 1

    def __str__(self) -> str:
        return str(self.wl)

class Monkey:
    items = []
    op_val = 0
    op_op = None
    div_test = 1
    true_monkey = 0
    false_monkey = 0

    def __init__(self, items, op_op, op_val, div_test, true_monkey, false_monkey) -> None:
        self.items = items
        self.op_op = op_op
        self.op_val = op_val
        self.div_test = div_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

round = 1
monkies = []
# monkies = [
    # Monkey([Item(79),Item(98)], "*", 19, 23, 2, 3),
    # Monkey([Item(54),Item(65),Item(75),Item(74)], "+", 6, 19, 2, 0),
    # Monkey([Item(79),Item(60),Item(97)], "*", "old", 13, 1, 3),
    # Monkey([Item(74)], "+", 3, 17, 0, 1),
# ]

monkies = [
    Monkey([Item(75), Item(75), Item(98), Item(97), Item(79), Item(97), Item(64)], "*", 13, 19, 2, 7),
    Monkey([Item(50), Item(99), Item(80), Item(84), Item(65), Item(95)], "+", 2, 3, 4, 5),
    Monkey([Item(96), Item(74), Item(68), Item(96), Item(56), Item(71), Item(75), Item(53)], "+", 1, 11, 7, 3),
    Monkey([Item(83), Item(96), Item(86), Item(58), Item(92)], "+", 8, 17, 6, 1),
    Monkey([Item(99)], "*", "old", 5, 0, 5),
    Monkey([Item(60), Item(54), Item(83)], "+", 4, 2, 2, 0),
    Monkey([Item(77), Item(67)], "*", 17, 13, 4, 1),
    Monkey([Item(95), Item(65), Item(58), Item(76)], "+", 5, 7, 3, 6),
]


def add_item(item, monkey_id):
    monkies[monkey_id].items.append(item)

def print_monkies():
    for i, m in enumerate(monkies):
        print("monkey %d: %s" % (i, ",".join(str(wl) for wl in m.items)))

inspects = []
for m in monkies:
    inspects.append(0)

for j in range(10000):
    for i, m in enumerate(monkies):
        # print("Monkey %d:" % i)
        for item in m.items:
            # print("inspecting item with worry level %d" % item.wl)
            inspects[i] += 1
            if m.op_op == "*":
                if m.op_val == "old":
                    item.wl *= item.wl
                else:
                    item.wl *= m.op_val
                item.wl = item.wl % 9699690
            elif m.op_op == "+":
                if m.op_val == "old":
                    item.wl += item.wl
                else:
                    item.wl += m.op_val
            # print("worry level mult by %s to %d" % (m.op_val, item.wl))
            # print("worry level mult by %s" % (m.op_val))
            
            if item.wl % m.div_test == 0:
                # print("wl divisble by %d, throwing to monkey %d" % (m.div_test, m.true_monkey))
                target_monkey = m.true_monkey
            else:
                # print("wl NOT divisble by %d, throwing to monkey %d" % (m.div_test, m.false_monkey))
                target_monkey = m.false_monkey
            add_item(item, target_monkey)
            # print()
        m.items = []
    round += 1
    print("after round ", j)
    print_monkies()

inspects.sort(reverse=True)
print(inspects)
print(inspects[0] * inspects[1])