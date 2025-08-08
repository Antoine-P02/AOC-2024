
def naive(source):
    file = open(source, "r")
    line = file.readlines()
    tmp = list(line[0])

    tab = getUnpacked(tmp)
    print("data unpacked")

    for x in range(len(tab) - 1, -1, -1):
        if (len(tab) - 1 - x) % (len(tab) // 10) == 0:
            print(f"{((len(tab) - 1 - x) * 100) // len(tab)}%")
        if getFirstDotPos(tab) != -1:
            lastPos = getLastInt(tab)
            if(lastPos != -1):
                tab[getFirstDotPos(tab)] = tab[lastPos]
                tab[lastPos] = '.'
    print(tab)
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

print("Star1 : ", naive("input9"), "in ?? min")


def naive2(source):
    file = open(source, "r")
    lines = file.readlines()


print("Star2 : ", naive2("input9"), "in ?? min")