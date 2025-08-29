import copy

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    tab = []
    for line in lines:
        lineInfos = []
        for char in line:
            if char == '\n':
                continue
            char = char.replace('.', '10')
            lineInfos.append(int(char))
        tab.append(lineInfos)

    display(tab)
    spawns = getStarts(tab)
    score = 0
    print("Starting points", spawns)

    for spawn in spawns:
        tmp = findPath(tab, spawn, [], [], 0, 0, len(tab[0])-1, len(tab)-1)
        score += getScore(tmp)
        print("#", score)



def getStarts(tab):
    spawns = []
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if (tab[x][y] == 0):
                spawns.append((x, y, 0))
    return spawns

def getMoves(pos, minH, minW, maxH, maxW):
    near = []
    if pos[0] -1 >= minW:
        near.append( (pos[0] -1, pos[1]) )
    if pos[1] -1 >= minH:
        near.append( (pos[0], pos[1]-1) )
    if pos[0] + 1 <= maxW:
        near.append( (pos[0] +1, pos[1]) )
    if pos[1] + 1 <= maxH:
        near.append( (pos[0], pos[1]+1) )
    
    return near

def canMove(tab, pos, minH, minW, maxH, maxW):
    near = getMoves(pos, minH, minW, maxH, maxW)
    res = []
    for p in near:
        if (tab[p[0]][p[1]] == pos[2] +1):
            res.append( (p[0], p[1], tab[p[0]][p[1]] ) )
    return res


def move(tab, pos, newPos, trail):
    trailCopy = copy.deepcopy(trail)
    trailCopy = copy.deepcopy(trail)
    trailCopy.append(newPos)
    pos = (newPos[0], newPos[1], tab[newPos[0]][newPos[1]])

    return (pos, None, trailCopy)

def findPath(tab, pos, trail, final, minH, minW, maxH, maxW):
    if (pos[2] == 9):
        print("REACHED", trail)
        final.append(trail)
        return trail
    
    newMoves = canMove(tab, pos, minH, minW, maxH, maxW)
    
    for n in newMoves:
        pozCopy = copy.deepcopy(pos)
        trelCopy = copy.deepcopy(trail)
        (pozCopy, newPos, trelCopy) = move(tab, pozCopy, n, trelCopy)
        findPath(tab, pozCopy, trelCopy, final, minH, minW, maxH, maxW)
    
    return final

def getScore(liste):
    res = []
    for l in liste:
        if ( l[ len(l) -1 ] not in res):
            res.append( l[ len(l) -1 ])
    print("res", res)
    return len(res)

def display(tab):
    print("-" * (len(tab) * 3) )
    for lines in tab:
        for el in lines:
            if int(el) > 9:
                print(el, end=' ')
            else:
                print(el, end='  ')
        print()
    print("-" * (len(tab) * 3) )


#print("Star1 : ", naive("input10"), "in 120 min")



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    tab = []
    for line in lines:
        lineInfos = []
        for char in line:
            if char == '\n':
                continue
            char = char.replace('.', '10')
            lineInfos.append(int(char))
        tab.append(lineInfos)

    display(tab)
    spawns = getStarts(tab)
    score = 0
    print("Starting points", spawns)

    for spawn in spawns:
        tmp = findPath(tab, spawn, [], [], 0, 0, len(tab[0])-1, len(tab)-1)
        score += len(tmp)
        print("#", score)

print("Star2 : ", naive2("input10"), "in 2 min (actual king I already planned for this)")