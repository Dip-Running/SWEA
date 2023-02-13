import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans, Sum = 0, 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            for k in range(m):
                for l in range(m):
                    Sum += arr[i+k][j+l]
            ans = max(ans, Sum)
            Sum = 0

    print(f'#{tc} {ans}')