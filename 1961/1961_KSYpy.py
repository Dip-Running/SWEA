T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # N x N arr
    arr = [list(map(str, input().split())) for _ in range(N)]
    arr1 = [[0] * N for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    arr3 = [[0] * N for _ in range(N)]

    # 90도 회전
    for i in range(N):
        for j in range(N):
            arr1[j][N-i-1] = arr[i][j]

    # 180도 회전
    for i in range(N):
        for j in range(N):
            arr2[N-i-1][N-j-1] = arr[i][j]

    # 270도 회전
    for i in range(N):
        for j in range(N):
            arr3[N-j-1][i] = arr[i][j]

    print(f'#{test_case}')
    # print
    for i in range(N):
        print(''.join(str(n) for n in arr1[i]), ''.join(str(n) for n in arr2[i]), ''.join(str(n) for n in arr3[i]))