
def display(tab):
    print("-" * (len(tab) * 3) )
    for lines in tab:
        for el in lines:
            print(el, end='')
        print()
        
    print("-" * (len(tab) * 3) )

def count(tab, zone):
    c = 0
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if tab[x][y] == zone:
                if isAlone(tab, (x,y), zone):
                    c += 1
    return c

def getPerimeter(tab, zone):
    sectionCount = 0
    perimeters = [[zone + str(sectionCount), 0, []]]

    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if tab[x][y] == zone:
                if (hasNeighbor(tab, (x,y), zone) ):
                    if ( hasNeighborWithSection((x,y), perimeters[sectionCount][2]) ):
                            perimeters[sectionCount][1] += isIsolated(tab, (x,y), zone)
                            perimeters[sectionCount][2].append((x,y))
                    elif perimeters[sectionCount][2] != []:
                        print("P1", zone, (x,y), perimeters)
                        sectionCount += 1
                        perimeters.append([zone + str(sectionCount), isIsolated(tab, (x,y), zone), [(x,y)]])
                    else:
                        print("here ??", (x,y))
                        perimeters[0][1] += isIsolated(tab, (x,y), zone)
                        perimeters[0][2].append((x,y))
                elif isAlone(tab, (x,y), zone):
                    print("P2", zone, (x,y), perimeters)
                    sectionCount += 1
                    perimeters.append([zone + str(sectionCount), 4, (x,y)])
                else:
                    print("FUCK")

    return perimeters


def getArea(tab, zone):
    sectionCount = 0
    areas = [[zone + str(sectionCount), 0, []]]

    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if tab[x][y] == zone:
                if (hasNeighbor(tab, (x,y), zone) ):
                    if ( hasNeighborWithSection((x,y), areas[sectionCount][2]) ):
                        areas[sectionCount][1] += 1
                        areas[sectionCount][2].append((x,y))
                    elif areas[sectionCount][2] != []:
                        print("A1", zone, (x,y), areas)
                        sectionCount += 1
                        areas.append([zone + str(sectionCount), 1, [(x,y)]])
                    else:
                        areas[0][1] += 1
                        areas[0][2].append((x,y))
                elif isAlone(tab, (x,y), zone):
                    print("A2", zone, (x,y), areas)
                    sectionCount += 1
                    areas.append([zone + str(sectionCount), 1, [(x,y)]])
                else:
                    print("sFuck")

    return areas

def isAlone(tab, pos, zone):
    around = [
        (pos[0]-1, pos[1]),
        (pos[0]+1, pos[1]),
        (pos[0], pos[1]-1),
        (pos[0], pos[1]+1)
    ]
    for sides in around:
        if (sides[0] >= 0 and sides[0] < len(tab) and sides[1] >= 0 and sides[1] < len(tab[0])):
            if(tab[sides[0]][sides[1]] == zone):
                return False
    return True

def hasNeighbor(tab, pos, zone):
    if (pos[0]-1 >= 0 and tab[pos[0]-1][pos[1]] == zone):
        return True
    if (pos[0]+1 < len(tab) and tab[pos[0]+1][pos[1]] == zone):
        return True
    if (pos[1]-1 >= 0 and tab[pos[0]][pos[1]-1] == zone):
        return True
    if (pos[1]+1 < len(tab[0]) and tab[pos[0]][pos[1]+1] == zone):
        return True
    return False

def hasNeighborWithSection(pos, trail):
    if (trail == []):
        return True
    for positions in trail:
        #print("Checking", positions[0], pos[0], positions[1] + 1, pos[1])
        if ( pos[0] -1 == positions[0] and pos[1] - 1 == positions[1] ):
            return True
        if ( pos[0] -1 == positions[0] and pos[1] == positions[1] ):
            return True
        if ( pos[0] -1 == positions[0] and pos[1] + 1 == positions[1] ):
            return True
        if ( pos[0] == positions[0] and pos[1] -1 == positions[1] ):
            return True
    print("??", pos, trail)
    return False

def isIsolated(tab, pos, zone):
    currentPos = zone
    c = 0
    if (pos[0]-1 < 0 or ( pos[0] - 1 >= 0 and tab[pos[0]-1][pos[1]] != currentPos) ):
        c += 1
    if (pos[0]+1 > len(tab)-1 or ( pos[0] + 1 < len(tab) and tab[pos[0]+1][pos[1]] != currentPos) ):
        c += 1
    if (pos[1]-1 < 0 or ( pos[1] - 1 >= 0 and tab[pos[0]][pos[1]-1] != currentPos) ):
        c += 1
    if (pos[1]+1 > len(tab[0])-1 or ( pos[1] + 1 < len(tab[0]) and tab[pos[0]][pos[1]+1] != currentPos) ):
        c += 1
    return c

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    tab = []
    zones = []
    for line in lines:
        line = line[:-1]
        tab.append(line)
        for char in line:
            if char not in zones:
                zones.append(char)
    
    res = {}
    total = 0

    for zone in zones:
        perimeters = getPerimeter(tab, zone)
        for perimeter in perimeters:
            res[perimeter[0]] = {
                "area": 0,
                "perimeter": perimeter[1]
            }

        areas = getArea(tab, zone)
        for area in areas:
            if area[0] in res:
                res[area[0]]["area"] = area[1]

        if (len(perimeters) != len(areas)):
            print('Error | perimeters:', perimeters, '| areas:', areas)

    for results in res:
        total += (res[results]["area"] * res[results]["perimeter"])

    #display(tab)
    print(res)

    return total





# def naive2(source):
#     file = open(source, "r")
#     line = file.readlines()[0]


a = naive('inputA')
b = naive('inputB')
print( ("ERROR", a) if a != 140 else "OK - a")
print( ("ERROR", b) if b != 772 else "OK - b")

print("Star1 : ", naive("input12"), "in ?? min")

#print("Star2:", naive2("input12"), "in ?? min")