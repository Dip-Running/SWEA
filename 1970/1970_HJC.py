import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(len(arr)):
        arr[i] = n // money[i]
        n -= money[i] * arr[i]
    print(f'#{tc}')
    print(*arr)