import sys
sys.stdin = open('input.txt', 'r')
#---------------------------------#
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    Sum = 0
    # 극한의 인덱싱,,,
    for i in range(n//2 + 1):   # i는 0 1 2
        # print(i, n//2-i, n//2+i+1)
        # n을 2로 나누고 그게 중심점이니 -i, +(i+1) (슬라이싱 합 구할땐 뒷부분 + 1 해줘야함, for range처럼) 범위 sum 더함
        Sum += sum(arr[i][n//2 - i : n//2 + (i+1)])

    for i in range(n//2 + 1, n):    # i는 3 4
        # print(i, n//2 - (n-i-1), n//2 + (n-i))
        # i가 3, 4니까 n-i = 2, 1임, 나는 1, 0을 원하니 n-i-1
        # n을 2로 나누고 그 중심점을 기준으로 -(n-i-1), +(n-i-1) + 1(마찬가지로 구간 합 구할땐 + 1)
        Sum += sum(arr[i][n//2 - (n-i-1):n//2 + ((n-i-1) + 1)])
    print(f'#{tc} {Sum}')