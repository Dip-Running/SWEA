import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    _arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*_arr))
    ans = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if arr[i][j] == 1:
                flag = 1
            elif arr[i][j] == 2:
                if flag:
                    ans += 1
                    flag = 0
    print(f"#{tc} {ans}")