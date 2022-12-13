prev = None
cnt = 0

with open('./2inp') as f:
    lines = f.readlines()
    for i in range(2, len(lines)):
        s = int(lines[i]) + int(lines[i-1]) + int(lines[i-2])
        print("s is: ", s)
        if prev != None and s > prev:
            cnt += 1
        prev = s
print(cnt)