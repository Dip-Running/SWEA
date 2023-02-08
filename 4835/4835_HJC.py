# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    size, win = map(int, input().split())
    arr = list(map(int, input().split()))
    # 최대는 0, 최소는 제약조건에 따른 10000과 win을 곱해 설정
    Max, Min = 0, 10000*win
    # 10 3 -> 8회 = 10 - 3 + 1
    # 10 5 -> 6회 = 10 - 5 + 1
    for i in range(size - win + 1):
        Sum = 0
        for j in range(i, i+win):
            Sum += arr[j]
        if Max < Sum: Max = Sum
        if Min > Sum: Min = Sum
    print(f'#{test_case} {Max - Min}')