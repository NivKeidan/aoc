g = []

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        g.append(l)

# indexes_visible = {}

# row_debug = 99
# col_debug = 0

# def add_to_map(r, c):
#     global indexes_visible
#     if r == row_debug or c == col_debug:
#         print("adding (%s, %s) with value %s to map" % (r, c, g[r][c]))
#     if r not in indexes_visible:
#         indexes_visible[r] = {}
#     indexes_visible[r][c] = True

# # check rows from left
# print("from left")
# for i in range(len(g)):
#     last_seen_height = -1
#     for j in range(len(g[i])):
#         current_height = int(g[i][j])
#         if current_height > last_seen_height:
#             last_seen_height = current_height
#             add_to_map(i, j)

# # check rows from right
# print("from right")
# for i in range(len(g)):
#     last_seen_height = -1
#     for j in range(len(g[i])-1, -1, -1):
#         current_height = int(g[i][j])
#         if current_height > last_seen_height:
#             last_seen_height = current_height
#             add_to_map(i, j)

# # check columns from top
# print("from top")
# for i in range(len(g[0])):
#     last_seen_height = -1
#     for j in range(len(g)):
#         current_height = int(g[j][i])
#         if current_height > last_seen_height:
#             last_seen_height = current_height
#             add_to_map(j, i)

# # check columns from bottom
# print("from bottom")
# for i in range(len(g[0])):
#     last_seen_height = -1
#     for j in range(len(g)-1, -1, -1):
#         current_height = int(g[j][i])
#         if current_height > last_seen_height:
#             last_seen_height = current_height
#             add_to_map(j, i)

# try:
#     print(indexes_visible[row_debug].keys())
#     print(len(indexes_visible[row_debug].keys()))
# except KeyError:
#     pass
# cnt = 0
# for k in indexes_visible.values():
#     cnt += len(k.keys())

def calculate_scenic(r, c):
    h = int(g[r][c])
    
    # count up
    cu = 0
    for ri in range(r-1, -1, -1):
        if int(g[ri][c]) <= h:
            cu += 1
        if int(g[ri][c]) >= h:
            break

    # count down
    cd = 0
    for ri in range(r+1, len(g)):
        if int(g[ri][c]) <= h:
            cd += 1
        if int(g[ri][c]) >= h:
            break

    # count left
    cl = 0
    for ci in range(c-1, -1, -1):
        if int(g[r][ci]) <= h:
            cl += 1
        if int(g[r][ci]) >= h:
            break

    # count right
    cr = 0
    for ci in range(c+1, len(g)):
        if int(g[r][ci]) <= h:
            cr += 1
        if int(g[r][ci]) >= h:
            break
    print("(%s, %s): %d, %d, %d, %d" % (r, c, cu, cd, cl, cr))
    return cu * cd * cl * cr

max_scenic = 0
for i in range(len(g)):
    for j in range(len(g[0])):
        score = calculate_scenic(i, j)
        if score > max_scenic:
            max_scenic = score
print(max_scenic)