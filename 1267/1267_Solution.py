import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, 11):
    v, e = map(int, input().split())
    _map = [[0] * (v + 1) for _ in range(v + 1)]

    arr = list(map(int, input().split()))
    n = len(arr) // 2

    for i in range(n):
        row = arr[i * 2]
        col = arr[i * 2 + 1]
        _map[col][row] = 1

    result = []
    while True:
        if len(result) == v:
            break

        # #시작점 찾기
        start_col = []
        for col in range(1, len(_map)):
            if 1 not in _map[col] and col not in result:
                start_col.append(col)
        # print(start_col)

        for col in start_col:
            result.append(col)
            for row in range(len(_map)):
                _map[row][col] = 0
        # print(MyMap)

    print(f'#{tc}', end=" ")
    for i in result:
        print(f'{i}', end=" ")
    print()