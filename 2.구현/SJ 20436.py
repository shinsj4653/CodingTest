sL, sR = input().split()
typeStr = input()
time = 0
lx = 0
ly = 0
rx = 0
ry = 0

keyBoard = []
keyBoard.append(['q', 'w', 'e', 'r','t','y','u','i','o','p'])
keyBoard.append(['a', 's', 'd', 'f','g','h','j','k','l'])
keyBoard.append(['z', 'x', 'c', 'v','b','n','m'])

isZaum = []
isZaum.append([True, True, True, True, True, False, False, False, False, False])
isZaum.append([True, True, True, True, True, False, False, False, False])
isZaum.append([True, True, True, True, False, False, False])

allnotZero = False

for i in range(len(keyBoard)) :
    for j in range(len(keyBoard[i])) :
        if keyBoard[i][j] == sL :
            lx = i
            ly = j
        
        if keyBoard[i][j] == sR:
            rx = i
            ry = j
            
        if lx != 0 and ly != 0 and rx != 0 and ry != 0 :
            allnotZero = True
            break
        
    if allnotZero :
        break

for letter in typeStr : 
    leftTime = 0
    rightTime = 0
    letterX = 0
    letterY = 0
    
    for i in range(len(keyBoard)) :
        for j in range(len(keyBoard[i])) :
            if keyBoard[i][j] == letter :
                letterX = i
                letterY = j
                break
        
    if isZaum[letterX][letterY] == True :
        leftTime += abs(letterX - lx) + abs(letterY - ly)
        time += leftTime
        lx = letterX
        ly = letterY
        
    else :
        rightTime += abs(letterX - rx) + abs(letterY - ry)
        time += rightTime
        rx = letterX
        ry = letterY
    
    time += 1
    
print(time)