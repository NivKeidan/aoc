file_name = './4/inp'
board_size = 5

class BingoNumber:
    def __init__(self, v) -> None:
        self.num = int(v)
        self.isMarked = False

class Board:
    def __init__(self) -> None:
        self.cells = []

    def addRow(self, data):
        row = []
        for n in data.split():
            bn = BingoNumber(n)
            row.append(bn)
        self.cells.append(row)
    
    def isWinner(self):
        # check rows
        # print("checking rows")
        for row in self.cells:
            valid = True
            for n in row:
                # print("num: ", n.num)
                if not n.isMarked:
                    # print("OUT!")
                    valid = False
                    break
            if valid:
                # print("YES!!")
                return True

        # check columns
        for i in range(0, board_size):
            valid = True
            for row in self.cells:
                if not row[i].isMarked:
                    valid = False
                    break
            if valid:
                return True
        return False

    def sumUnmarked(self):
        sum = 0
        for row in self.cells:
            for n in row:
                if not n.isMarked:
                    sum += n.num
        return sum
    
    def mark_number(self, num):
        for row in self.cells:
            for n in row:
                if n.num == num:
                    n.isMarked = True
                    return True
        return False

boards = []
drawn_numbers = None

with open(file_name) as f:
    is_first_line = True
    current_board = None

    for l in f.readlines():
        l = l.strip()
        if l == "":
            if current_board is not None:
                boards.append(current_board)
                current_board = None
            continue
        if is_first_line:
            drawn_numbers = l.split(",")
            is_first_line = False
            continue
        if current_board is None:
            current_board = Board()
        current_board.addRow(l)
    boards.append(current_board)

board_nums = len(boards)
winners = []

for draw_num in drawn_numbers:
    draw_num = int(draw_num)
    print("%d drawn" % draw_num)
    
    for i, b in enumerate(boards):
        if i in winners:
            continue
        found = b.mark_number(draw_num)
        print("board %s - %s" % (i, "yes" if found else "no"))
        if b.isWinner():
            print("board %s wins" % i)
            if len(winners) == board_nums-1:
                print(b.sumUnmarked() * draw_num)
                exit(0)
            winners.append(i)