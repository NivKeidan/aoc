instructions = []
used = {}
accumulator = 0
nextInsIndex = 0
indexes_to_replace = []
to_replace = -1

def get_ins(ind):
    ins = instructions[ind][0]
    val = int(instructions[ind][1])
    return ins, val

# def crawl_back(ind, visited, has_change, path):
#     if ind == 0:
#         print("SUCCESS")
#         print(path)
#         print("change:", has_change)
#         exit()
#     if ind in visited:
#         return
#     visited[ind] = True
#     for i in range(len(instructions)):
#         print("now in %d, checking %d" % (ind, i))
#         print(get_ins(i))
#         if get_next_ind(i) == ind:
#             crawl_back(i, visited, has_change, path + [ind])
#         if has_change is None and get_next_ind_with_change(i) == ind:
#             crawl_back(i, visited, i, path + [ind])
    
#     print(path + [ind], end=" ")
#     if has_change is None:
#         print("no change")
#     else:
#         print("change on %d" % has_change)

# def get_next_ind(ind):
#     ins, val = get_ins(ind)
#     if ins == "acc" or ins == "nop":
#         return ind+1
#     if ins == "jmp":
#         return ind+val

# def get_next_ind_with_change(ind):
#     ins, val = get_ins(ind)
#     if ins == "acc" or ins == "jmp":
#         print(ind +1)
#         return ind + 1
#     if ins == "nop":
#         print(ind + val)
#         return ind + val
    

def execute_instruction(ind, first_run=False):
    global accumulator, nextInsIndex, used, indexes_to_replace, to_replace

    if ind == 591:
        print("this is it")
        print(accumulator)
        exit()
    
    ins, val = get_ins(ind)
    used[ind] = True
    
    if ind == to_replace:
        if ins == "jmp":
            ins = "nop"
        elif ins == "nop":
            ins = "jmp"
    
    if ins == "nop":
        nextInsIndex += 1
        if first_run:
            print("adding", ind)
            indexes_to_replace.append(ind)
    
    if ins == "acc":
        accumulator += val
        nextInsIndex += 1

    if ins == "jmp":
        nextInsIndex += val
        if first_run: 
            print("adding", ind)
            indexes_to_replace.append(ind)
    
    # if first_run: print(ind, ":", ins, val, "->", nextInsIndex)

    if nextInsIndex in used:
        print(accumulator)
        return
    execute_instruction(nextInsIndex, first_run)

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        parts = l.split(" ")
        instruction = parts[0]
        value = parts[1]
        instructions.append((instruction, value))

execute_instruction(nextInsIndex, True)
# for ind in indexes_to_replace:
#     print("replacing", ind)
#     to_replace = ind
#     nextInsIndex = 0
#     accumulator = 0
#     used = {}
#     execute_instruction(nextInsIndex, False)

# start = len(instructions)
# crawl_back(start, {}, None, [])