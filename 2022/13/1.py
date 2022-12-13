IN_ORDER = 1
NOT_IN_ORDER = -1
DONT_KNOW = 0

def is_list(o):
    return isinstance(o, list)

def is_in_order(a, b):
    if not is_list(a) and not is_list(b):
        inta = int(a)
        intb = int(b)
        if inta < intb:
            return IN_ORDER
        if inta > intb:
            return NOT_IN_ORDER
        return DONT_KNOW    

    if is_list(a) and is_list(b):
        lena = len(a)
        lenb = len(b)
        for i in range(min(lena, lenb)):
            res = is_in_order(a[i], b[i])
            if res != DONT_KNOW:
                return res

        if lena < lenb:
            return IN_ORDER
        elif lena > lenb:
            return NOT_IN_ORDER
        return DONT_KNOW
    
    # one int, one list
    if is_list(a):
        return is_in_order(a, [b])
    else:
        return is_in_order([a], b)

# is_new = True
# a = None
# b = None
# sum = 0
# cnt = 0
all_packets = []
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        if l == "":
            continue
        all_packets.append(eval(l))
    all_packets.append([[2]])
    all_packets.append([[6]])

        # if l == "":
            # cnt += 1
            # in_order = is_in_order(a, b)
            # if in_order == IN_ORDER:
            #     sum += cnt
            # is_new = True
            # a = None
            # b = None
            # continue
        
        # if is_new == True:
        #     a = eval(l)
        #     is_new = False
        # else:
        #     b = eval(l)
import functools
sorted_l = sorted(all_packets, key=functools.cmp_to_key(is_in_order), reverse=True)
s = 1
for i, p in enumerate(sorted_l):
    print(p)
    if p == [[2]]:
        s *= i +1
    if p == [[6]]:
        s *= i+1
print(s)