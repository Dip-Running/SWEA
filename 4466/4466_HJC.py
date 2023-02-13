import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    Sum = 0
    for i in range(k):
        Sum += arr.pop(arr.index(max(arr)))
    print(f'#{tc} {Sum}')