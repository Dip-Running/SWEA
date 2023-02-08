# import sys
# sys.stdin = open('input.txt', 'r')

# 2차원 배열 0으로 선언, 건물이 존재하는 위치에 1로 저장
# 이중 반복문을 사용하여 해당 층의 해당 건물이 존재하는 위치에서
# 양옆으로 두칸씩 확인해서 전부 0이면 cnt ++, 탐색 다하면 print(cnt)
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    # 행은 제약조건(건물의 최대높이)에 따름
    Fac = [[0] * n for _ in range(255)]
    arr = list(map(int, input().split()))
    for i in range(255):
        for j in range(n): # arr값이 높이, 이걸 층이라 가정하면
            if arr[j] > i:  # i는 i번째 층을 의미함
                Fac[i][j] = 1   # i층의 j번째에는 건물이 있음

    cnt = 0
    for i in range(255):    # 한층씩 탐색
        stack = 0
        for j in range(n):  # 특정 층에 특정 위치에 건물이 있다?
            if Fac[i][j] == 1:
                # 양옆 2칸씩 다 0인지 확인
                if Fac[i][j-2] == 0 and \
                    Fac[i][j-1] == 0 and \
                    Fac[i][j+1] == 0 and \
                    Fac[i][j+2] == 0:
                    # 다 0이면 cnt ++
                    cnt += 1
    print(f"#{test_case} {cnt}")