# import sys
# sys.stdin = open('input.txt', 'r')
# 1이 빨강, 2가 파랑
# 전체 10 * 10 배열 선언 후
# 같은색이 칠해져 있지 않으면
# 해당 부위에 색깔만큼 +
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    # 10 * 10 2차원 배열 0으로 초기화
    coor = [[0] * 10 for _ in range(10)]
    pos = []
    for i in range(n):
        pos.append(list(map(int,input().split())))  # 색칠 정보 추가
    for i in pos:
        color = i[-1]
        # x 좌표만큼(항상 [2] 보다 [0]이 작음)
        for x in range(i[0], i[2] + 1):
            # y 좌표만큼(항상 [3] 보다 [1]이 작음)
            for y in range(i[1], i[3] + 1):
                # 색깔이 이미 칠해져 있는게 아니라면
                if coor[x][y] != color:
                    # 해당 색칠정보의 색깔만큼 더함
                    coor[x][y] += color
    # 위 작업이 끝나면 10*10은 0 또는 1 또는 2 또는 3으로 채워져있음
    # 3이 보라색

    # 전체 배열 돌면서 3 갯수 카운트
    cnt = 0
    for i in range(10):
        for j in range(10):
            if coor[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
