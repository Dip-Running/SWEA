import sys
sys.stdin = open('input.txt', 'r')
# 위상정렬

T = 5
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))
    data = []
    n = len(arr)
    for i in range(0, n, 2):
        data.append([arr[i], arr[i+1]])
    print(data)
    for i in range(len(data)):
        if