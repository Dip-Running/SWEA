T = int(input())

for test_case in range(1, T + 1):
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]
    print(f"#{test_case}")
    for i in range(size):
        for j in range(size):
            print(arr[size - 1 - j][i], end='')
        print(end=' ')
        for j in range(size):
            print(arr[size - 1 - i][size - 1 - j], end='')
        print(end=' ')
        for j in range(size):
            print(arr[j][size - 1 - i], end='')
        print('')