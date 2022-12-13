file_name = "./8/inp"
total_sum = 0
letters = "abcdefg"

with open(file_name) as f:
    for l in f.readlines():
        l = l.strip()
        [patterns, rest] = [x for x in l.split("|")]

        f = {} # codes -> number
        rf = {} # num -> code
        codes = {}  # a/b/c.../g -> temp number

        fives = []
        sixes = []

        for p in patterns.split():
            p = "".join(sorted(p))
            if len(p) == 2:
                f[p] = 1
                rf[1] = p
            elif len(p) == 3:
                f[p] = 7
                rf[7] = p
            elif len(p) == 4:
                f[p] = 4
                rf[4] = p
            elif len(p) == 7:
                f[p] = 8
                rf[8] = p
            
            elif len(p) == 5:  # 2/3/5
                fives.append("".join(sorted(p)))
            elif len(p) == 6:  # 6/9/0
                sixes.append("".join(sorted(p)))
        
        # find d
        for l in rf[4]:
            if l not in rf[1]:
                valid = True
                for five_opt in fives:
                    if l not in five_opt:
                        valid = False
                        break
                if valid:
                    codes['d'] = l
                    break
        
        # find 0
        for s in sixes:
            if codes['d'] not in s:
                rf[0] = s
                f[s] = 0
                sixes.remove(s)
                break
        
        # find 6
        for s in sixes:
            for l in letters:
                if l not in s:
                    if l in rf[4]:
                        rf[6] = s
                        sixes.remove(s)
                        f[s] = 6

        # find 9
        nine = sixes[0]
        rf[9] = nine
        f[nine] = 9

        # find 3 - all letters in 3 exist in at least one other five
        for fiv in fives:
            valid = True
            fives_cp = fives.copy()
            fives_cp.remove(fiv)
            for l in fiv:
                if l not in fives_cp[0] and l not in fives_cp[1]:
                    valid = False
                    break
            if valid:
                three = fiv
                rf[3] = three
                f[three] = 3
                fives.remove(fiv)
                
                break
            if valid:
                break

        # find 2
        missing_in_6 = None
        for l in letters:
            if l not in rf[6]:
                missing_in_6 = l
                break
        for five_opt in fives:
            if l in five_opt:
                two = five_opt
                rf[2] = two
                f[two] = 2
                fives.remove(five_opt)
                break

        # find 5
        five = fives[0]
        rf[5] = five
        f[five] = 5

        multiplier = 1000
        for n in rest.split():
            n = "".join(sorted(n))
            total_sum += f[n] * multiplier
            multiplier = multiplier / 10
print(total_sum)