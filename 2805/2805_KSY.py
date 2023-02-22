# import sys
# sys.stdin = open('input.txt')

T = int(input())    # test case
for test_case in range(1, T + 1):
    N = int(input())    # N X N arr
    field = [list(map(int, input())) for _ in range(N)]
    increase = N // 2 + 1
    cnt_list = []

    for i in range(increase):   # 증가하는 절반만
        cnt_list.append(field[i][N//2-i:N//2+i+1])

    for i in range(N-1, increase-1, -1):    # 감소하는 절반만
        cnt_list.append(field[i][N // 2 - (N-i)+1:N // 2 + (N-i)])

    # print(cnt_list)
    # 합계 구하기
    total = 0
    for lst in cnt_list:
        for i in range(len(lst)):
            total += lst[i]

    print(f'#{test_case}', total)

