# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    # 양의 정수 - 최대를 0, 제약조건에 따라 최소를 1000000
    Max, Min = 0, 1000000
    for i in arr:
        if Max < i:
            Max = i
        if Min > i:
            Min = i
    print(f'#{test_case} {Max - Min}')