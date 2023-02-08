# import sys
# sys.stdin = open('input.txt')

T = 10  # 테스트 케이스의 개수

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]  # 이차원 배열(행렬)

    sumi_list = []
    sumj_list = []

    for i in range(100):
        sumi_list.append(sum(arr[i]))
        maxi = max(sumi_list)   # 가로 합 중에 최댓값


    for i in range(100):
        col = 0
        for j in range(100):
            col += arr[j][i]
        sumj_list.append(col)
        maxj = max(sumj_list)   # 세로 합 중에 최댓값

    # print(maxi, maxj)
    # i = j 인 대각선의 합
    total1 = total2 = 0
    for i in range(100):
        total1 += arr[i][i]
    # print(total1)

    # i는 증가하고 j는 감소하는 대각선의 합
    for i in range(100):
        total2 += arr[i][99-i]
    # print(total2)

    real_max = max(maxi, maxj, total1, total2)
    print(f'#{n} {real_max}')



