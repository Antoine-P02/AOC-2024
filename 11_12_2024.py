def naive(source):
    file = open(source, "r")
    line = file.readlines()[0]

    data = []
    tmp = list(line.split(' '))
    for char in tmp:
        data.append(int(char))

    print(data)

    for x in range(25):
        index = 0
        while index < len(data):
            data, index = stoneAction(data[index], index, data)

    return len(data)


def stoneAction(stoneValue, index, stoneList):
    if (stoneValue == 0):
        stoneValue = 1
        stoneList[index] = stoneValue

    elif (len(str(stoneValue)) % 2 == 0):
        stoneString = str(stoneValue)
        stoneValue = ''
        newStone = ''

        for x in range( int(len(stoneString)/2) ):
            stoneValue += stoneString[x]
            newStone += stoneString[ x + int(len(stoneString)/2) ]

        stoneValue = int(stoneValue)
        newStone = int(newStone)
        stoneList[index] = stoneValue
        index += 1
        stoneList.insert(index, newStone)
    else:
        stoneValue = 2024  * stoneValue
        stoneList[index] = stoneValue

    
    return stoneList, index+1
    




#print("Star1 : ", naive("input11"), "in 40 min")



def rec(stoneValue):
    if (stoneValue == 0):
        return [1]

    elif (len(str(stoneValue)) % 2 == 0):

        stoneString = str(stoneValue)

        mid = len(stoneString) // 2
        stoneValue = stoneString[:mid]
        newStone = stoneString[mid:]
        return [int(stoneValue), int(newStone)]

    else:
        return [stoneValue * 2024]

def getResponse(visited, value, depth):
    if (depth >= 75):
        return 1

    res = (value, depth)

    if res in visited:
        return visited[res]
    
    results = 0
    for new in rec(value):
        results += getResponse(visited, new, depth + 1 )
    visited[res] = results

    return results


def optimized(dataList):
    visited = {}
    score = 0
    for x in range(len(dataList)):
        score += getResponse(visited, dataList[x], 0)
        print(x, len(visited))
    return score

def naive2(source):
    file = open(source, "r")
    line = file.readlines()[0]

    data = []
    tmp = list(line.split(' '))
    for char in tmp:
        data.append(int(char))

    print(data)
    return optimized(data)



print("Star2:", naive2("input11"), "in 180 min")
