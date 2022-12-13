file_name = './5/inp'
start = 0
end = 1000


class Point:
    def __init__(self, x, y) -> None:
        self.x = int(y)
        self.y = int(x)
        self.counter = 0
    
    def __repr__(self) -> str:
        return "(%d,%d) - %d" % (self.x, self.y, self.counter)

class Line:
    def __init__(self, pt_s, pt_e) -> None:
        self.start = pt_s
        self.end = pt_e

class Grid:
    def __init__(self) -> None:
        self.cells = []

        for i in range(start, end):
            self.cells.append([])
            for j in range(start, end):
                self.cells[i].append(Point(i, j))
    
    def __repr__(self) -> str:
        final = ""
        for i, r in enumerate(self.cells):
            row = "(%d) " % i
            for c in r:
                if c.counter == 0:
                    row += "."
                else:
                    row += str(c.counter)
            final += "\n%s" % row
        return final

    def mark(self, l):
        if l.start.y == l.end.y:
            print("same y")
            step_y = 0
            step_x = -1 if l.start.x > l.end.x else 1
            num_of_points = abs(l.start.x - l.end.x)
        elif l.start.x == l.end.x:
            print("same x")
            step_x = 0
            step_y = -1 if l.start.y > l.end.y else 1
            num_of_points = abs(l.start.y - l.end.y)
        elif abs(l.start.x - l.end.x) == abs(l.start.y - l.end.y):
            print("diag")
            step_x = -1 if l.start.x > l.end.x else 1
            step_y = -1 if l.start.y > l.end.y else 1
            num_of_points = abs(l.start.x - l.end.x)
        else:
            print("skipping line (%d,%d)->(%d,%d)" % (l.start.x, l.start.y, l.end.x, l.end.y))
            return

        for i in range(0, num_of_points+1):
            self.cells[l.start.x + (step_x*i)][l.start.y + (step_y*i)].counter += 1
        # print(grid)
        # input()
        
grid = Grid()

with open(file_name) as f:
    for l in f.readlines():
        l = l.strip()
        print("handling %s" % l)

        s, e = l.split(" -> ")
        sx, sy = s.split(",")
        ex, ey = e.split(",")
        ptStart = Point(sx, sy)
        ptEnd = Point(ex, ey)
        line = Line(ptStart, ptEnd)

        grid.mark(line)

cnt = 0
for r in grid.cells:
    for p in r:
        if p.counter > 1:
            cnt += 1
print(cnt)