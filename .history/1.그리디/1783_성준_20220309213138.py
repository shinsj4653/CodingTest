n, m = input().split()
n = int(n)
m = int(m)

chess = [[0 for col in range(m)] for row in range(n)]

x = n - 1 # 나이트의 세로위치
y = 0 # 나이트의 가로위치

chess[x][y] = 1 # 시작점

