import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # 전체크기, 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]   # N x N 2차원 리스트


<<<<<<< HEAD
    fly_list = []
    for j in range(N-M+2):
        for i in range(N-M+1):
            fly_list.append(arr[j][i:i+M])
    # print(fly_list)
    total = [0] * len(fly_list)
    for i in range(21):    # 24개
        total[i] = fly_list[i] + fly_list[i+N-1]
    print(total)
=======
    fly_list = [[] * N for _ in range((N-1)*(N-1))]
    # 파리채 안에 들어올 숫자들
    # 한 줄 먼저 계산해보기
    # for i in range(M):
    #     for k in range(N-M+1):
    #         for j in range(k, M+k):
    #             fly_list[k].append(arr[i][j])
    # 열 계산도 해주기
    for l in range(N-M+1):
        for i in range(l, M+l):
            for k in range(N-M+1):
                for j in range(k, M+k):
                    fly_list[k+(N-1)*l].append(arr[i][j])


    # print(fly_list)
    sum_list = []
    for lst in fly_list:    
        sum_list.append(sum(lst))   # fly_list 중에 합이 가장 큰 걸 구하기
    print(f'#{tc} {max(sum_list)}')

>>>>>>> 3c83e54604bb9e2f205dd585f21df414602f1ea3
