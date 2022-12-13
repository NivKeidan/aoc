import bisect
arr = []
connected = []
m = {}

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        n = int(l)

        bisect.insort(arr, n)

device = arr[-1]+3
arr += [device]
print(arr)
def valid_paths(chain, starting_index):
    if starting_index in m:
        return m[starting_index]
    if starting_index == len(arr)-1:
        print(chain)
        return 1
    current_jolt = chain[-1]

    path_counter = 0
    for i in range(1, 4):
        try:
            val = arr[starting_index+i]
        except IndexError:
            break
        if val - current_jolt <= 3:
            path_counter += valid_paths(chain + [val], starting_index+i)
    m[starting_index] = path_counter
    return path_counter
print(valid_paths([0], -1))

# current_jolt = 0
# for a in arr + [device]:
#     if a - current_jolt <= 3:
#         current_jolt += a
#         connected.append(a)
#     print(connected)

# current_jolt = 0
# ones = 0
# threes = 0

# for c in connected:
#     if c - current_jolt == 1:
#         ones += 1
#     if c - current_jolt == 3:
#         threes += 1
#     current_jolt = c
# print(ones * threes)
