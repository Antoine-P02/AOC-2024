import copy 
import numpy as np

def getNextGuardPos(pos, direct):
    return pos[0] + direct[0], pos[1] + direct[1] 

def isIn(pos, liste):
    minX = 0
    maxX = len(liste)
    minY = 0
    maxY = len(liste[0][0])
    return ( minX <= pos[0] < maxX and minY <= pos[1] < maxY)

def getRight(direct):
    points = [ (-1,0), (0,+1), (+1,0), (0,-1) ]
    ###########North , East,    South,  West

    return points[ (points.index(direct) +1) % 4 ]


def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    tab = []

    for x in range(len(lines)):
        tab.append( lines[x].split())
        for y in range( len(lines[x]) ):
            if lines[x][y] in ["^", "<",">", "v"]:
                guard = x, y

    direction = (-1,0)

    lineTest = list(tab[guard[0]][0].strip())
    lineTest[guard[1]] = '9'
    tab[guard[0]][0] = ''.join(lineTest)
    
    nextGuardPos = getNextGuardPos(guard, direction)



    while isIn(nextGuardPos, tab):
        while tab[nextGuardPos[0]][0][nextGuardPos[1]] != '#' :

            new = getNextGuardPos(nextGuardPos, direction)
            lineTest = list(tab[nextGuardPos[0]][0].strip())
            lineTest[nextGuardPos[1]] = '9'
            tab[nextGuardPos[0]][0] = ''.join(lineTest)

            if isIn(new, tab):
            
                if tab[new[0]][0][new[1]] != '#':
                    nextGuardPos = new

                else:
                    break
            else:
                nextGuardPos = new
                break
            

        if isIn(nextGuardPos, tab):
            direction = getRight(direction)
        
        
        
    res = 0
    
    print("-"*150)
    for t in tab:
        #print(t)
        for string in t[0]:
            if string == '9':
                res +=1
    
    return res
    
print("Star1 : ", naive("input6"), "in 175 min")


def getNextGuardPos2(pos, direct):
    return pos[0] + direct[0], pos[1] + direct[1] 

def isIn2(pos, liste):
    minX = liste[0]
    maxX = liste[1]
    minY = liste[2]
    maxY = liste[3]
    return ( minX <= pos[0] < maxX and minY <= pos[1] < maxY)

def getRight2(direct):
    points = [ (-1,0), (0,+1), (+1,0), (0,-1) ]
    ###########North , East,    South,  West

    return points[ (points.index(direct) +1) % 4 ]


def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    visited = {}
    res = 0

    res_stored = []

    rows, cols = len(lines), len(lines[0]) 
    tab = np.zeros((rows, cols), dtype=int)

    for a in range(rows):
        for b in range(cols):

            if lines[a][b] == '#':
                tab[a, b] = 1

            elif lines[a][b] in ["^", "<", ">", "v"]:
                guard = a,b
                tab[a, b] = 0 

            else:
                tab[a, b] = 0 
    
    dimensions = np.array([0, len(tab), 0, len(tab[0]) ])
    
    for x in range(rows):
        for y in range(cols):

            if (x,y) == (82, 42) or (x,y) == (5,4):
                break

            if (x,y) != guard and tab[x][y] == 0:

                tabCopy = copy.deepcopy(tab)

                tabCopy[x][y] = 1

                direction = (-1,0)

                visited[guard] = 1

                
                nextGuardPos = getNextGuardPos2(guard, direction)

                goNext = False

                while isIn2(nextGuardPos, dimensions):
                    while tabCopy[nextGuardPos[0]][nextGuardPos[1]] != 1 and not goNext:

                        if nextGuardPos in visited:

                            if visited[nextGuardPos] > 2:
                                print("loop", x,y)
                                goNext = True
                                res += 1
                                res_stored.append((x,y))
                            
                            visited[nextGuardPos] += 1 


                            
                        
                        else:
                            visited[nextGuardPos] = 1

                        new = getNextGuardPos2(nextGuardPos, direction)
                        if isIn2(new, dimensions):
                        
                            if tabCopy[new[0]][new[1]] == 0:
                                nextGuardPos = new
                            else:
                                break
                        else:
                            nextGuardPos = new
                            break
                        
                            
                        
                    if goNext:
                        break
                    elif isIn2(nextGuardPos, dimensions):
                        direction = getRight2(direction)

            visited = {}
    
    for sto in res_stored:
        tab[sto[0]][sto[1]] = 5
    tab[guard[0]][guard[1]] = 3
    
    for ta in tab:
        print(ta)
    
    return res


print("Star2 : ", naive2("input6"), "in Star1 + ?? min")

