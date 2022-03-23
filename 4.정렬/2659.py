clock = list(map(int, input().split()))
clockNum = 0
answer = 0

def clock_num(c) : 
    start = 0
    clockl = []
    
    for i in range(4) :
        start = i
        num = 0
        for j in range(4) :
            num += (c[start]) * (10 ** (3 - j))
            if start + 1 == 4 :
                start = 0
            else :
                start += 1

        clockl.append(num)

    clockl.sort()
    return clockl[0]

clockNum = clock_num(clock)

for i in range(1111, clockNum + 1) :
    strNum = str(i)
    c = []
    for s in strNum :
        c.append(int(s))

    if i == clock_num(c) :
        answer += 1    

print(answer)