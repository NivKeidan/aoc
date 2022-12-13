group_ht = {}
group_size = 0
cnt = 0

with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()

        if l == "":
            for k, v in group_ht.items():
                if v == group_size:
                    cnt += 1
            group_ht = {}
            group_size = 0
            continue

        group_size += 1
        for ans in l.strip():
            if ans not in group_ht:
                group_ht[ans] = 0
            group_ht[ans] += 1

    for k, v in group_ht.items():
        if v == group_size:
            cnt += 1
    
print(cnt)