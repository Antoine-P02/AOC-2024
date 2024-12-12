

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0
    storedPairs = []

    for x in lines:

        if len(x) == 6:
            before = int( x[0:2] )
            after =  int( x[3:5] )

            if before not in storedPairs or after not in storedPairs:
                storedPairs.append( [before, after] )

        elif len(x) > 6:
            toSort = x[0:len(x)-1].split(',')
            toSortList = []
            for z in toSort:
                toSortList.append(int(z))

            if verify(toSortList, storedPairs):
                current = toSortList[ int( len(toSortList) /2 ) ]
                res += current
            current = 0


    return res


def verify(current, sortedPairs):
    for num in current:
        indexNum = current.index(num)

        for num2 in current:
            if num == num2:
                pass
            
            indexNum2 = current.index(num2)

            if [num, num2] in sortedPairs:
                if indexNum > indexNum2:
                    return False
            
            if [num2, num] in sortedPairs:
                if indexNum2 > indexNum:
                    return False
    return True


print("Star1 : ", naive("input5"), "in 75 min")

def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0
    storedPairs = []

    for x in lines:

        if len(x) == 6:
            before = int( x[0:2] )
            after =  int( x[3:5] )

            if before not in storedPairs or after not in storedPairs:
                storedPairs.append( [before, after] )

        elif len(x) > 6:
            toSort = x[0:len(x)-1].split(',')
            toSortList = []
            for z in toSort:
                toSortList.append(int(z))

            passCheck = verify(toSortList, storedPairs)

            if (not passCheck):
                while not passCheck:
                    
                    for num in toSortList:
                        indexNum = toSortList.index(num)
                        for num2 in toSortList:
                            if num == num2:
                                pass
                            indexNum2 = toSortList.index(num2)

                            if [num, num2] in storedPairs:
                                if indexNum > indexNum2:

                                    toSortList[indexNum], toSortList[indexNum2] = toSortList[indexNum2], toSortList[indexNum]
                                    indexNum, indexNum2 = indexNum2, indexNum 
                            
                            elif [num2, num] in storedPairs:
                                if indexNum2 > indexNum:

                                    toSortList[indexNum], toSortList[indexNum2] = toSortList[indexNum2], toSortList[indexNum]
                                    indexNum, indexNum2 = indexNum2, indexNum 

                    
                    passCheck = verify(toSortList, storedPairs)

                res += toSortList[ int( len(toSortList) /2 ) ]

    return res




print("Star2 : ", naive2("input5"), "in Star1 + 30 min")

