import sys
N = int(sys.stdin.readline())
board = [[" "] * (4*N-3) for _ in range(4*N-3)]

def star(pos, n):
    if n == 0:
        return

    pos_end = pos+4*n-3
    for i in range(pos, pos_end):         #y축에 대하여 반복
        for j in range(pos, pos_end):     #x축에 대하여 반복
            if i==pos or j==pos or i== pos_end-1 or j==pos_end-1:       #pos를 기준으로 x, y가 첫줄이거나 마지막줄일때
                board[i][j] = "*"
    star(pos+2, n-1)

star(0, N)

for i in board:
    print(''.join(i))
