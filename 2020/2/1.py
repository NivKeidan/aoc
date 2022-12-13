counter=0
with open('inp1') as f:
    for l in f.readlines():
        l = l.strip()
        parts = l.split(" ")
        minMax = parts[0].split("-")
        
        ind1 = int(minMax[0])
        ind2 = int(minMax[1])
        letter = parts[1][:1]
        word = parts[2]

        try:
            in1 = word[ind1-1] == letter
        except IndexError:
            in1 = False
    
        try:
            in2 = word[ind2-1] == letter
        except IndexError:
            in2 = False
        
        if in1 and not in2 or in2 and not in1:
            print(in1, in2)
            counter += 1
print(counter)