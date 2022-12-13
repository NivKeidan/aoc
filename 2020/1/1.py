ht = {}

with open('inp1', 'r') as input:
    for l in input.readlines():
        l = l.strip()   
        if l == "":
            continue
        ht[l] = True
    print(ht)
    for e in ht.keys():
        expense = int(e)
        match = 2020-expense
        # print("num is ", e, "looking for", match)
        if str(2020 - int(e)) in ht:
            print(int(e) * (2020-int(e)))
            exit(0)