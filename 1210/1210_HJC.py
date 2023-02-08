# import sys
# sys.stdin = open('input.txt', 'r')
#------------------------#
T = 10
dx,dy = [0, 0], [-1, 1]
for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    N = len(arr)
    for ind in range(N):
        if arr[-1][ind] == 2:   # 정답 찾았을 때
            x, y = N-1, ind
            while True:
                if x == 0:
                    print(f'#{tc} {y}')
                    break
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                        while 0 <= ny < N and arr[nx][ny] == 1:
                            y = ny
                            arr[x][y] = 0
                            ny += dy[i]
                else:
                    x -= 1
                if x >= N:
                    break