import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [False for i in range(n+1)]
    cnt = list(map(int, input().split()))

    arr[0] = True
    for i in range(m):
        arr[cnt.pop()] = True

    print(f'#{tc} ', end='')
    for i in range(len(arr)):
        if not arr[i]:
            print(i, end=' ')
    print()