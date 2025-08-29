
def naive(source):
    file = open(source, "r")
    line = file.readlines()
    tmp = list(line[0])

    tab = getUnpacked(tmp)
    print("data unpacked")

    for x in range(len(tab) - 1, -1, -1):
        if (len(tab) > 1000):
            if (len(tab) - 1 - x) % (len(tab) // 10) == 0:
                print(f"{((len(tab) - 1 - x) * 100) // len(tab)}%")
        if getFirstDotPos(tab) != -1:
            if (getFirstDotPos(tab)  < getLastInt(tab)):
                #print("dot", getFirstDotPos(tab), "last", getLastInt(tab))
                lastPos = getLastInt(tab)
                tab[getFirstDotPos(tab)] = tab[lastPos]
                tab[lastPos] = '.'
                
    print(len(tab), tab)
    return getSum(tab)

def getUnpacked(data):
    res = []
    c = 0
    for x in range(len(data)):
        point = int(data[x])
        if (x % 2 == 0):
            char = str(c)
            c += 1
        else:
            char = '.'
        
        for y in range(point):
            res.append(char)
    return res

def getSum(res):
    count = 0
    for z in range(len(res)):
        if (res[z] != '.'):
            count += (z * int(res[z]))
    return count

def getFirstDotPos(liste):
    if ('.' in liste):
        return liste.index('.')
    return -1

def getLastInt(liste):
    for y in range(len(liste) - 1, -1, -1):
        if liste[y] != '.':
            return y
    return -1

#print("Star1 : ", naive("input9"), "in ?? min")


def naive2(source):
    file = open(source, "r")
    line = file.readlines()
    tmp = list(line[0])

    tab = getUnpacked(tmp)
    print("data unpacked", str(tab).replace("', '", ''))

    dotSeries = []
    series = []
    x = 0
    while x < len(tab):
        if (tab[x] == '.'):
            dot = getOrderedSerie(tab, x)
            dotSeries.append(dot)
            x = max(dot[2]+1, x+1)

        else:
            serie = getOrderedSerie(tab, x)
            series.append(serie)
            x = max(serie[2]+1, x+1)

    series.reverse()
    finalTab = replace(tab, dotSeries, series)
    print(str(finalTab).replace("', '", ''))
    return getSum(finalTab)

def swap(tab, dot, ints):
    for x in range(ints[1], ints[2]+1, 1):
        x = x - ints[1]
        # replace dot with int
        tab[dot[1] + x] = tab[ints[1] + x]

        #replace int previous pos with dot
        tab[ints[1] + x] = '.'
    return tab



def replace(tab, dotSeries, series):
    x = 0
    while x < len(dotSeries):
        dotSerie = dotSeries[x]
        for serie in series:
            if dotSerie[1] < serie[1]:
                if (serie[0] > dotSerie[0]):
                    a = 0
                elif (serie[0] == dotSerie[0]):
                    tab = swap(tab, dotSerie, serie)
                    series.remove(serie)
                    break
                else:
                    tab = swap(tab, dotSerie, serie)
                    series.remove(serie)
                    dotLen = dotSerie[0] - serie[0]
                    dotStart = dotSerie[2] + 1 - dotLen
                    dotEnd = dotSerie[2] 
                    remainingDot = (dotLen, dotStart, dotEnd)
                    dotSeries.insert(x+1, remainingDot)
                    break
        x += 1
    return tab


def getOrderedSerie(tab, index):
    current = tab[index]
    res = 0
    newPos = index
    while tab[newPos] == current:
        res +=1
        if newPos < len(tab) - 1:
            newPos += 1
        else:
            break
    if newPos != len(tab) - 1:
        newPos -= 1
    return (res, index, newPos)

def getReversedSerie(tab, index):
    current = tab[index]
    res = 0
    newPos = index
    while tab[newPos] == current:
        res +=1
        if newPos >=  1:
            newPos -= 1
        else:
            break
    return (res, index, newPos-1)


print("Star2 : ", naive2("input9"), "in 75 min")