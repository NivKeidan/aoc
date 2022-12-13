tickets = [None] * 127

with open('inp1') as f:
    for lc, l in enumerate(f.readlines()):
        l = l.strip()
        row = l[:7]
        seat = l[7:]
        row2 = [None] * 7
        seat2 = [None] * 3

        for i, c in enumerate(row):
            if c == "F":
                row2[i] = "0"
            if c == "B":
                row2[i] = "1"
        
        for i, c in enumerate(seat):
            if c == "L":
                seat2[i] = "0"
            if c == "R":
                seat2[i] = "1"
        
        row2 = int("".join(row2), 2)
        seat2 = int("".join(seat2), 2)
        if tickets[row2] == None:
            tickets[row2] = []
        tickets[row2].append(seat2)
        # code = row2 * 8 + seat2

for i, row in enumerate(tickets):
    if row is not None and len(row) < 8:
        print(i, row)

print(80*8+2)
