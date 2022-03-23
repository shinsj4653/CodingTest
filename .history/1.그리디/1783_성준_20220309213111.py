n, m = input().split()
n = int(n)
m = int(m)

chess = [[0 for col in range(m)] for row in range(n)]
# print(chess)

x = n - 1
y = 0

chess[x][y] = 1
print(chess)