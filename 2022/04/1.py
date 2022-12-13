cnt = 0
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        first, second = l.split(",")
        min1, max1 = first.split("-")
        min2, max2 = second.split("-")
        min1 = int(min1)
        max1 = int(max1)
        min2 = int(min2)
        max2 = int(max2)

        if max1 < min2 or max2 < min1:
            continue
        cnt += 1
print(cnt)