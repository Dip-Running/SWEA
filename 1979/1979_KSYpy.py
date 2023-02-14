import sys
sys.stdin = open('input.txt')

T = int(input())    # 테스트 케이스의 개수
for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N: 가로세로길이, K: 단어의 길이
    row_arr = [list(map(int, input().split())) for _ in range(N)]  # 2차원 리스트로 받기
    col_arr = [[0] * N for _ in range(N)]   # 이차원리스트를 세로로 받아보자

    for i in range(N):
        for j in range(N):
            col_arr[i][j] = row_arr[j][i]

    total = 0
    for i in range(N):     # 이중포문 행 리스트
        cnt = 0
        for j in range(N):
            if row_arr[i][j] == 0: # 0 이고
                if cnt == K:  # cnt = K 이면
                    total += 1 # total에 1 더해주고
                cnt = 0  # cnt는 다시 0
            else:   # 0 아니면
                cnt += 1 # cnt +1
        if cnt == K:    # cnt가 k이면
            total += 1  # 1추가

    for i in range(N):     # 이중포문 열 리스트
        cnt = 0
        for j in range(N):
            if col_arr[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1


    print(f'#{tc} {total}')






