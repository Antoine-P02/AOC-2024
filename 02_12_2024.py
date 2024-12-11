
def naive(source):
    file = open(source, "r")
    lines = file.readlines()
    tmpInt = ''
    inputData = []
    for line in lines:
        tmpInput = []
        for ch in line:

            if ch == ' ':
                if tmpInt != '':
                    tmpInput.append( int(tmpInt) )
                    tmpInt = ''

            elif ch in "0123456789":
                tmpInt += ch

            elif ch == '\n':
                tmpInput.append( int(tmpInt) )
                inputData.append(tmpInput)
                tmpInput = []
                tmpInt = ''
    
    tmpInput.append( int(tmpInt) )
    inputData.append(tmpInput)

    safe = 0
    for x in inputData:
        safe += loop(x)
    return safe
        
        

def loop(l):
    if len(l) <= 1:
        return 1
    
    compare = l[0]
    
    ascOrder = l[1] > l[0]

    for y in range(1, len(l), 1):

        if ascOrder:
            if ( compareOrder( compare, l[y] ) ) or l[y] - 3 > compare:
                return 0
            compare = l[y]

        else :
            if ( compareOrder( l[y], compare ) ) or compare - 3 >  l[y] :
                return 0
            compare = l[y]

    
    
    if ascOrder:
        print(l, 1, l == sorted(l) )
    else:
        print(l, 1, l == sorted(l, reverse=True) )
            
    
            
    return 1


def compareOrder(a, b):
    return a >= b



print(naive("input2"))


def naive2(source):
    file = open(source, "r")
    lines = file.readlines()
    tmpInt = ''
    inputData = []
    for line in lines:
        tmpInput = []
        for ch in line:

            if ch == ' ':
                if tmpInt != '':
                    tmpInput.append( int(tmpInt) )
                    tmpInt = ''

            elif ch in "0123456789":
                tmpInt += ch

            elif ch == '\n':
                tmpInput.append( int(tmpInt) )
                inputData.append(tmpInput)
                tmpInput = []
                tmpInt = ''
    
    tmpInput.append( int(tmpInt) )
    inputData.append(tmpInput)

    safe = 0
    for x in inputData:
        safe += loop2(x)
    return safe


def loop2(l):
    for x in l:
        copy = l.copy()
        copy.remove(x)
        if loop(copy) == 1:
            return 1
    return 0

print(naive2("input2"))