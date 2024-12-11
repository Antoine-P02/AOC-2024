

def naive(source):
    file = open(source, "r")
    lines = file.readlines()
    tmpInt = ''
    inputData = []
    for line in lines:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if tmpInt != '':
                    inputData.append( int(tmpInt) )
                    tmpInt = ''
            elif ch in "0123456789":
                tmpInt += ch

    inputData.append( int(tmpInt) )
    file.close()

    left = []
    right = []

    for x in range(0, len(inputData), 2):
        left.append(inputData[x])
        right.append(inputData[x+1])

    left.sort()
    right.sort()
    res = 0

    for x in range(len(left)):
        res += max(left[x], right[x]) - min(left[x], right[x])
    return res

def precise(source):

    file = open(source, "r")
    lines = file.readlines()

    left = {}
    right = {}

    tmpInt = ''
    inputData = []
    leftSide = True

    for line in lines:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if tmpInt != '':

                    if (leftSide):
                        left.update( { int(tmpInt) } )
                        leftSide = False
                    else:
                        right.update( { int(tmpInt) } )
                        leftSide = True

                    tmpInt = ''
            elif ch in "0123456789":
                tmpInt += ch

    res = 0
    while left != {}:
        val1 = min(left)
        val2 = min(right)
        res += max(val1, val2) - min(val1, val2)
        left.remove(val1)
        right.remove(val2)
    return res



print(naive("input1"))
#print(precise("input1")) #fucked, no idea if ints are repeated



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()
    tmpInt = ''
    inputData = []
    for line in lines:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if tmpInt != '':
                    inputData.append( int(tmpInt) )
                    tmpInt = ''
            elif ch in "0123456789":
                tmpInt += ch

    inputData.append( int(tmpInt) )
    file.close()

    left = []
    right = []

    for x in range(0, len(inputData), 2):
        left.append(inputData[x])
        right.append(inputData[x+1])

    visited = []
    res = 0
    for z in left:
        if z in right:
            c = 0
            while z in right:
                c +=1
                right.remove(z)
            res += c * z
    return res


def precise2(source):
    file = open(source, "r")
    lines = file.readlines()
    tmpInt = ''
    inputData = []
    for line in lines:
        for ch in line:
            if ch == ' ' or ch == '\n':
                if tmpInt != '':
                    inputData.append( int(tmpInt) )
                    tmpInt = ''
            elif ch in "0123456789":
                tmpInt += ch

    inputData.append( int(tmpInt) )
    file.close()

    left = []
    right = []

    for x in range(0, len(inputData), 2):
        left.append(inputData[x])
        right.append(inputData[x+1])

    visited = []
    res = 0
    for z in left:
        res += z * right.count(z) 
    return res

print(naive2("input1"))
print(precise2("input1"))


