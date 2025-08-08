import copy







# def evaluate(result, varList, operatorList):
    
#     res = varList[0]
#     for x in range(len(operatorList)):
#         res = eval(res)
#         expr = "'" + str(res) + operatorList[x] + varList[x+1] + "'"
#         res = eval(expr)

#     if (eval(res) == result):
#         return 1
#     else:
#         return 0

# def nextStep(result, varList, operatorList, originalList, index):
#     data = copy.deepcopy(originalList)

#     if (len(data) == 0 ):
#         return evaluate(result, varList, operatorList)
#     else:
#         #print("????????????", result, varList, operatorList, data, index)
#         varList = varList.copy()
#         operatorList = operatorList.copy()

#         operators = ["*", "+"]
#         if (len(data) != 1):
#             operatorList.append(operators[index])
#         varList.append(data[0])
#         data = data[1:]
#         #print("aaaaaa", result, varList, operatorList, data, index)
#         #print()

#         varList = varList.copy()
#         operatorList = operatorList.copy()

#         if(nextStep(result, varList, operatorList, data, 0)):
#             return True
        
#         if(nextStep(result, varList, operatorList, data, 1)):
#             return True
        
#         return 0

# def isPossible2(result, data):
#     one = nextStep(result, [], [], data, 0)
#     two = nextStep(result, [], [], data, 1)

#     if (one or two):
#         return result
#     else: 
#         return 0

# def naive(source):
#     file = open(source, "r")
#     lines = file.readlines()

#     finalCount = 0
#     c = 0
#     c1 = 0

#     for x in range(len(lines)):
#         result, data = lines[x].split(":")
#         result = int(result)
#         data = data.strip().split()
#         res = isPossible(result, data)
#         finalCount += res
#         c +=1
#         if (res > 0 ):
#             c1 += 1
#     print(c, c1, finalCount)
#     return finalCount

# #print("Star1 : ", naive("input7"), "in 105 min")







def fuse(left, right):
    return str(left) + str(right)

def evaluate2(result, varList, operatorList):
    
    res = varList[0]
    for x in range(len(operatorList)):
        if int(res) > result:
            return 0
        if (operatorList[x] == '||'):
            res = int(fuse(res, varList[x+1]))
        else:
            expr = "'" + str(res) + operatorList[x] + varList[x+1] + "'"
            res = eval(expr)
            res = eval(res)    
    if (res == result):
        return 1
    else:
        return 0

def nextStep2(result, varList, operatorList, originalList, index):
    data = copy.deepcopy(originalList)

    if (len(data) == 0 ):
        return evaluate2(result, varList, operatorList)
    else:
        varList = varList.copy()
        operatorList = operatorList.copy()

        operators = ["*", "+", "||"]
        if (len(data) > 1):
            operatorList.append(operators[index])
        varList.append(data[0])
        data = data[1:]

        varList = varList.copy()
        operatorList = operatorList.copy()

        if(nextStep2(result, varList, operatorList, data, 0)):
            return True
        
        if(nextStep2(result, varList, operatorList, data, 1)):
            return True
        
        if(nextStep2(result, varList, operatorList, data, 2)):
            return True
        return 0

def isPossible2(result, data):
    one = nextStep2(result, [], [], data, 0)
    two = nextStep2(result, [], [], data, 1)
    three = nextStep2(result, [], [], data, 2)

    if (one or two or three):
        return result
    else: 
        return 0

def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    finalCount = 0

    for x in range(len(lines)):
        print(x)
        result, data = lines[x].split(":")
        result = int(result)
        data = data.strip().split()
        res = isPossible2(result, data)
        finalCount += res

    return finalCount

print("Star2 : ", naive2("input7"), "in 30 min")