import sys

sys.stdin = open('input.txt', 'r')
'''
사각형 내부에는 빈 용기가 없음
사각형 사이에는 빈 용기가 있음
대각선 사이에는 빈 용기가 없을 수 있음
전체 행렬을 돌며 값이 등장하면 행렬의 크기를 측정함
행렬의 크기, 행의 크기 순으로 정렬해서 출력할 것
'''


def check(x, y):  # x, y : 용기에 액체가 담겨있는 최솟값
    stX, stY = x, y  # 현재 위치 기억
    col, row = 1, 1
    # 행 탐색
    while True:
        nx = x + 1
        if arr[nx][y]:
            x = nx
            col += 1
        else:
            break
    # 열 탐색
    while True:
        ny = y + 1
        if arr[x][ny]:
            y = ny
            row += 1
        else:
            break

    for _i in range(stX, stX + col):
        for _j in range(stY, stY + row):
            visited[_i][_j] = True
    return [col, row]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            # 0이 아닌 값 & 방문하지 않은 지점이라면 돌면서 행렬 크기 측정
            if arr[i][j] and not visited[i][j]:
                ans.append(check(i, j))
    # 행렬의 크기를 우선으로, 같은 사이즈라면 x[0] 즉, 행의 길이 우선으로 정렬
    ans = sorted(ans, key=lambda x: (x[0] * x[1], x[0]))
    # 출력
    print(f'#{tc} {len(ans)} ', end='')
    for i in ans:
        print(*i, end=' ')
    print()
