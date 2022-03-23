# def move(x, y, chess) :
  
#   if (x - 2 < 0 or y + 1 > m - 1) or (x - 1 < 0 or y + 2 > m - 1) or (x + 1 > n - 1 or y + 2 > m - 1) or (x + 2 > n - 1 or y + 1 > m - 1) :
#     return
#   else :
#     if (x - 2 >= 0 and y + 1 <= m - 1) :
#       x -= 2
#       y += 1
#       chess[x][y] = 1
#       move(x, y, chess)

#     elif (x - 1 >= 0  and y + 2 <= m - 1) :
#       x -= 1
#       y += 2
#       chess[x][y] = 1
#       move(x, y, chess)

#     elif (x + 1 <= n - 1  and y + 2 <= m - 1) :
#       x += 1
#       y += 2
#       chess[x][y] = 1
#       move(x, y, chess)

#     elif (x + 2 <= n - 1  and y + 1 <= m - 1) :
#       x += 2
#       y += 1
#       chess[x][y] = 1
#       move(x, y, chess)

#chess = [[0 for col in range(m)] for row in range(n)]

#x = n - 1 # 나이트의 세로위치
#y = 0 # 나이트의 가로위치
n, m = map(int, input().split())
visited = 0 

if n == 1 :
  visited = 1

elif n == 2 :
  if m <= 2 :
    visited = 1
  else :
    visited = ((m - 1) // 2) + 1

else :
  if m <= 4 :
    visited = m
  
  elif m == 5 :
    visited = 4
    
  elif m >= 6 :
    visited = (m - 5) + 3
    

print(visited)


