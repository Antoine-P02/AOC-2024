

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    mulDone = False        #-> MUL(    
    beforeComa = False      #-> MUL( int,
    stringPairs = []        #-> [] | -> ["int"] | ["int", "int"]

    currentString = ''

    for line in lines:
        for ch in line:

            if ch == 'm':
                if len(currentString) == 0:
                    currentString = ch
                    print("#",currentString,"#")
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False
            
        
            elif ch == 'u':
                if len(currentString) == 1:
                    currentString += ch
                    print("#",currentString,"#")
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                    
            elif ch == 'l':
                if len(currentString) == 2:
                    currentString += ch
                    print("#",currentString,"#")
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False
            
            elif ch == '(' :
                if len(currentString) == 3:
                    mulDone = True
                    currentString += ch
                    print("#",currentString,"#")
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False


            elif ch in "0123456789":
                if (mulDone):
                    lastChar = currentString[ len(currentString) -1 ]
                    if ( lastChar in "0123456789" or lastChar == '(' ) or (lastChar == ',' and beforeComa):
                        
                        if (not beforeComa):
                            if ( len(stringPairs) == 0 ):
                                stringPairs.append(ch)
                            else:
                                stringPairs[0] += ch
                        else:
                            if (len(stringPairs) == 1 ):
                                stringPairs.append(ch)
                            else:
                                stringPairs[1] += ch

                        currentString += ch
                        print("#",currentString,"#")

                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
            
            elif ch == ',' :
                if (mulDone and len(stringPairs) > 0 ):
                    currentString += ch
                    beforeComa = True
                    print("#",currentString,"#")
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False


            elif ch == ')' :
                if (len(stringPairs) == 2):
                    res += int( stringPairs[0] ) * int( stringPairs[1])
                    currentString += ch
                    print("#",currentString,"#\n")

                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False
            
            else:
                mulDone, currentString, stringPairs, beforeComa = False, '', [], False

    return res





print("Star1 :", naive("input3"), "in ≈ 75min in 2 sessions")


def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    INACTIVE = False

    mulDone = False        #-> MUL(    
    beforeComa = False      #-> MUL( int,
    stringPairs = []        #-> [] | -> ["int"] | ["int", "int"]

    currentString = ''

    for line in lines:
        for ch in range(len(line)):

            if len(line) - ch > 4:
                if (line[ch:ch+4] == "do()"):
                    INACTIVE = False
                elif (line[ch:ch+7] == "don't()"):
                    INACTIVE = True

            if INACTIVE:
                pass
            else:

                if line[ch] == 'm':
                    if len(currentString) == 0:
                        currentString = line[ch]     
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                
            
                elif line[ch] == 'u':
                    if len(currentString) == 1:
                        currentString += line[ch]
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                        
                elif line[ch] == 'l':
                    if len(currentString) == 2:
                        currentString += line[ch]      
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                
                elif line[ch] == '(' :
                    if len(currentString) == 3:
                        mulDone = True
                        currentString += line[ch]
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False


                elif line[ch] in "0123456789":
                    if (mulDone):
                        lastChar = currentString[ len(currentString) -1 ]
                        if ( lastChar in "0123456789" or lastChar == '(' ) or (lastChar == ',' and beforeComa):
                            if (not beforeComa):
                                if ( len(stringPairs) == 0 ):
                                    stringPairs.append(line[ch])
                                else:
                                    stringPairs[0] += line[ch]
                            else:
                                if (len(stringPairs) == 1 ):
                                    stringPairs.append(line[ch])
                                else:
                                    stringPairs[1] += line[ch]

                            currentString += line[ch]
                            

                        else:
                            mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                
                elif line[ch] == ',' :
                    if (mulDone and len(stringPairs) > 0 ):
                        currentString += line[ch]
                        beforeComa = True
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False


                elif line[ch] == ')' :
                    if (len(stringPairs) == 2):
                        res += int( stringPairs[0] ) * int( stringPairs[1])
                        currentString += line[ch]

                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                    else:
                        mulDone, currentString, stringPairs, beforeComa = False, '', [], False
                
                else:
                    mulDone, currentString, stringPairs, beforeComa = False, '', [], False

    return res



print("Star2 : ", naive2("input3"), "in Star1 + 15min")

#175700056
