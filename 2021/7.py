import  statistics
file_name = "./7/inp"
locations = []

with open(file_name) as f:
    for l in f.readlines():
        l = l.strip()
        locations = [int(x) for x in l.split(",")]

mean = statistics.mean(locations)
# print(mean)
s = 0

for l in locations:
    diff = abs(l-462)
    print("diff is %d" % diff)
    ts = 0
    for i in range(0, diff):
        ts += diff-i
    print("ts: %d" % ts)
    s += ts
    # input()
print(s)

# 461 96678050
# 462 96678103