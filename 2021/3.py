length = 12
file_name = "./3/inp"

ox_all = []
oc_all = []

with open(file_name) as f:
    for l in f.readlines():
        l = l.strip()
        oc_all.append(l)
        ox_all.append(l)

def get_target(ind, options, type):
    cnt = 0
    for o in options:
        if o[ind] == "0":
            cnt += 1
        else:
            cnt -= 1
    
    if cnt > 0:  # more 0s than 1s
        if type == "ox":
            return "0"
        else:
            return "1"
    elif cnt < 0:
        if type == "ox":
            return "1"
        else:
            return "0"
    else:  # equal
        if type == "ox":
            return "1"
        else:
            return "0"

def do_calc(options, type):
    for bitIndex in range(0, length+1):
        print("index: ", bitIndex)
        if len(options) == 1:
            return int(options[0], 2)
        else:
            target = get_target(bitIndex, options, type)
            print("target is: ", target)
            new_options = []
            for o in options:  
                print(o, end="")
                if o[bitIndex] == target:
                    print(" - yep")
                    new_options.append(o)
                else:
                    print(" - no")
            options = new_options
        # input()

oxf = do_calc(ox_all, "ox")
ocf = do_calc(oc_all, "oc")
print(oxf, ocf)
print(oxf * ocf)
