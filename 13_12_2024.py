def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    data = []
    for x in range(0, len(lines), 4):
        a = lines[x].replace(      'Button A: X+', '').replace(' Y+', '')
        b = lines[x+1].replace(    'Button B: X+', '').replace(' Y+', '')
        prize = lines[x+2].replace('Prize: X=', '').replace(' Y=', '')
        tmp = {
            "A": getDict(a),
            "B": getDict(b),
            "Prize": getDict(prize)
        }

        bigX, bigY = tmp['A']
        smallX, smallY = tmp['B']
        prizeX, prizeY = tmp['Prize']

        possible_solutions = []

        for (ax, ay, bx, by) in [(bigX, bigY, smallX, smallY), (smallX, smallY, bigX, bigY)]:
            resX = solveX(ax, bx, prizeX)
            resY = solveY(ay, by, prizeY)
            if resX is not None and resY is not None:
                if resX[1] == resY[1]:
                    cost = resX[0]*3 + resX[1]
                    possible_solutions.append(cost)

        if possible_solutions:
            data.append(min(possible_solutions))
        else:
            data.append(None)

    print(data)
    return solve(data)

def solve(data):
    score = 0
    for d in data:
        if d != None:
            score += d
        
    return score

def solveX(big, small, goal):
    score = 0
    for z in range(100, 0, -1):
        remainder = (goal - (big * z)) / small
        if remainder > 0 and int(remainder) == remainder:
            score = z * big + remainder * small
            res = (z, remainder)
            break
    if score == goal:
        return res
    else:
        return None

def solveY(big, small, goal):
    score = 0
    for z in range(100, 0, -1):
        remainder = (goal - (big * z)) / small
        if remainder > 0 and int(remainder) == remainder:
            score = z * big + remainder * small
            res = (z, remainder)
            break
    if score == goal:
        return res
    else:
        return None
    
def getDict(txt):
    x = ''
    y = ''
    flag = False
    for z in range(len(txt)):
        if txt[z] == '\n':
            continue
        if txt[z] == ",":
            flag = True
        elif flag:
            y += txt[z]
        else:
            x += txt[z]
    return (int(x), int(y))

#print("Star1 : ", naive("input13"), "in 180 min")



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    data = []
    for x in range(0, len(lines), 4):
        print("Processing block:", x, "of", len(lines) /4)
        a = lines[x].replace(      'Button A: X+', '').replace(' Y+', '')
        b = lines[x+1].replace(    'Button B: X+', '').replace(' Y+', '')
        prize = lines[x+2].replace('Prize: X=', '').replace(' Y=', '')
        tmp = {
            "A": getDict(a),
            "B": getDict(b),
            "Prize": getDict(prize)
        }

        bigX, bigY = tmp['A']
        smallX, smallY = tmp['B']
        prizeX, prizeY = tmp['Prize']
        prizeX += 10000000000000
        prizeY += 10000000000000

        possible_solutions = []

        for (ax, ay, bx, by) in [(bigX, bigY, smallX, smallY), (smallX, smallY, bigX, bigY)]:
            resX = solveX2(ax, bx, prizeX)
            resY = solveY2(ay, by, prizeY)
            if resX is not None and resY is not None:
                if resX[1] == resY[1]:
                    cost = resX[0]*3 + resX[1]
                    possible_solutions.append(cost)

        if possible_solutions:
            data.append(min(possible_solutions))
        else:
            data.append(None)

    print(data)
    return solve(data)



def solveX2(big, small, goal):
    score = 0
    limit = (goal // big) -1
    for z in range(limit, 0, -1):
        remainder = (goal - (big * z)) / small
        if remainder > 0 and int(remainder) == remainder:
            score = z * big + remainder * small
            res = (z, remainder)
            break
    if score == goal:
        return res
    else:
        return None

def solveY2(big, small, goal):
    score = 0
    limit = (goal // big) -1
    for z in range(limit, 0, -1):
        remainder = (goal - (big * z)) / small
        if remainder > 0 and int(remainder) == remainder:
            score = z * big + remainder * small
            res = (z, remainder)
            break
    if score == goal:
        return res
    else:
        return None

print("Star2:", naive2("input13"), "in giveup after 40 min")
