

def naive(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    vs = []

    for x in range(len(lines)):
        line = lines[x]
        vLine = ''

        res += ( line.count('XMAS')  )
        res += ( line.count('SAMX')  )

        for y in range(len(line)-1):
            
            if len(line) - 4 >= 2 and len(lines) - x >= 4:
                if lines[x][y] == 'X':
                    if lines[x+1][y+1] == 'M':
                        if lines[x+2][y+2] == 'A':
                            if lines[x+3][y+3] == 'S':
                                res += 1
            
            if len(line) - 4 >= 2 and len(lines) - x >= 4:
                if lines[x][y] == 'S':
                    if lines[x+1][y+1] == 'A':
                        if lines[x+2][y+2] == 'M':
                            if lines[x+3][y+3] == 'X':
                                res += 1

            if y >= 3 and len(lines) - x >= 4:
                if lines[x][y] == 'X':
                    if lines[x+1][y-1] == 'M':
                        if lines[x+2][y-2] == 'A':
                            if lines[x+3][y-3] == 'S':
                                res += 1
            
            if y >= 3 and len(lines) - x >= 4:
                if lines[x][y] == 'S':
                    if lines[x+1][y-1] == 'A':
                        if lines[x+2][y-2] == 'M':
                            if lines[x+3][y-3] == 'X':
                                res += 1

            vLine += lines[y][x]
        
        vs.append(vLine)

    for v in vs:
        res += ( v.count('XMAS')  )
        res += ( v.count('SAMX')  )

    return res


print("Star1 : ", naive("input4"), "in 120min")



def naive2(source):
    file = open(source, "r")
    lines = file.readlines()

    res = 0

    minBound = 1
    maxBound = len(lines) -2

    for x in range(len(lines)):
        line = lines[x]
       

        for y in range(len(line)-1):

            if line[y] == 'A':

                if ( minBound <= x <= maxBound and minBound <= y <= maxBound):

                    if ( ''.join(sorted(lines[x-1][y-1] + lines[x+1][y+1])) == 'MS' and ''.join(sorted(lines[x-1][y+1] + lines[x+1][y-1])) == 'MS'):
                        res += 1

            
           
    return res


print("Star2 : ", naive("input4"), "in 20min")


