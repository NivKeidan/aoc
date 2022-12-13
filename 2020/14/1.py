mem = {}
mask = None

def num_to_blist(n):
    return list('{:036b}'.format(n))

def blist_to_num(l):
    return int("".join(l), 2)

def get_indexes_to_change(ind):
    print("getting indexes for", "".join(ind))
    # input(mask)
    return get_indexes(mask, 0, ind)

def get_indexes(mask_to_index, ind, original_index_b36):
    print(mask_to_index)
    if ind >= len(mask_to_index):
        return [mask_to_index]
    current_char = mask_to_index[ind]
    if current_char == "0":
        return get_indexes(mask_to_index[:ind] + original_index_b36[ind] + mask_to_index[ind+1:], ind+1, original_index_b36)
    if current_char == "1":
        return get_indexes(mask_to_index, ind+1, original_index_b36)
    if current_char == "X":
        return get_indexes(mask_to_index[:ind] + "0" + mask_to_index[ind+1:], ind+1, original_index_b36) + \
        get_indexes(mask_to_index[:ind] + "1" + mask_to_index[ind+1:], ind+1, original_index_b36)

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        
        vr, eq, vl = l.split(" ")
        if vr == "mask":
            mask = vl
        else:
            ind = vr[4:-1]
            ind_36b = num_to_blist(int(ind))
            indexes_to_change = get_indexes_to_change(ind_36b)
            for ind in indexes_to_change:
                mem[ind] = int(vl)

s = 0
for v in mem.values():
    s += v
print(s)


# for mem_addr, val in mem.items():
#     val_32b = list('{:036b}'.format(val))

#     print(val_32b)
#     print(list(mask))
#     for c in changes:
#         val_32b[c[0]] = c[1]
#     print(val_32b)
#     mem[mem_addr] = int("".join(val_32b), 2)