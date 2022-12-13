max_depth = 0

def parse_line(l):
    r = r"\([0-9+ *]+\)"
    
    # find deepest
    # convert all parantheses
    # go from left to right, replace every two with result
    # move on

with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()

        r = parse_line(l)
