T = int(input())
for tt in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))
    print(f'#{tt} {max(num)-min(num)}')