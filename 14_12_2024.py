class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.robots = []
        self.cells = []
        self.create_Board()

    def create_Board(self):
        for x in range(self.width):
            row = []
            for y in range(self.height):
                cell = Cell(x, y)
                row.append(cell)
            self.cells.append(row)

    def add_robot(self, robot):
        self.cells[robot[0][0]][robot[0][1]].value.append(robot[1])

    def display(self):
        for row in self.cells:
            for cell in row:
                print(cell, end="")
            print()

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = []

    def __repr__(self):
        if self.value == []:
            return "."
        elif len(self.value) == 1:
            return "R"
        else:
            return "X"


def naive(source):
    file = open(source, "r")
    lines = file.readlines()
    
    robots = []
    for line in lines:
        stringRobot = line.replace('p=', '').replace('v=', '').replace('\n', '')
        p, v = stringRobot.split(' ')
        p0, p1 = p.split(',')
        v0, v1 = v.split(',')
        robot = [ (int(p0), int(p1)), (int(v0), int(v1)), "r" + str(len(robots))]
        robots.append(robot)

    Bo = Board(11, 7)
    for robot in robots:
        Bo.add_robot(robot)
    Bo.display()


def display(board):
    for row in board:
        print("".join(row))
    print()

print("Star1 : ", naive("input14"), "in 180 min")



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()



print("Star2:", naive2("input14"), "in ?? min")
