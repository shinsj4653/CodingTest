n, m = input().split()
n = int(n)
m = int(m)

chess = [[0 for col in range(m)] for row in range(n)]

x = n - 1 # 나이트의 세로위치
y = 0 # 나이트의 가로위치

chess[x][y] = 1 # 시작점

def move(x, y) :
  if (x - 2 < 0 and y + 1 > m - 1) or (x - 1 < 0 and y + 2 > m - 1) or (x + 1 > n - 1 and y + 2 > m - 1) or (x + 2 > n - 1 and y + 1 > m - 1) :
    return
  
  else :
    if not (x - 2 < 0 and y + 1 > m - 1) :
      x -= 2
      y += 1
      chess[x][y] = 1
      move(x, y)
    
    elif not (x - 1 < 0 and y + 2 > m - 1) :
      x -= 1
      y += 2
      chess[x][y] = 1
      move(x, y)
      
    elif not (x + 1 > n - 1 and y + 2 > m - 1) :
      x += 1
      y += 2
      chess[x][y] = 1
      move(x, y)
      
    elif not (x + 2 > n - 1 and y + 1 > m - 1) :
      x += 2
      y += 1
      chess[x][y] = 1
      move(x, y)
      

count = chess.count(1)
print(count)
