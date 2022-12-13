to_save = 14

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
    for i in range(len(l)):
        if i < to_save:
            continue
        founds = []
        print("now in index ", i)
        for j in range(1, to_save+1):
            c = l[i-j]
            print("checking char %s at index %d" % (c, i-j))
            if c in founds:
                print("already found")
                break
            print("new")
            founds.append(c)
        if len(founds) == to_save:
            print("got it:", i)
            exit()
