T = int(input())

for test_case in range(1,   T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))
    Max = Sum = 0

    if N > M:                   # A가 더 클때
        for i in range(0, N - M + 1):
            Sum = 0
            for j in range(0, M):
                Sum = Sum + (A[i + j] * B[j])
            if Max < Sum:
                Max = Sum

    else:                       # B가 더 클때
        for i in range(0, M - N + 1):
            Sum = 0
            for j in range(0, N):
                Sum = Sum + (A[j] * B[i + j])
            if Max < Sum:
                Max = Sum

    print("#", test_case, sep='', end='')
    print("",Max)
