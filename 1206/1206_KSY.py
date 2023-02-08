T = 10    # 테스트 케이스의 개수
# import sys
# sys.stdin = open('1206input.txt')

for tc in range(T):
    N = int(input())    # 건물의 개수
    building = list(map(int, input().split()))
    count = 0

    for i in range(N-4):
        a = building[i]
        b = building[i+1]
        c = building[i+3]
        d = building[i+4]


        # 조망권을 구하고 싶은 빌딩을 기준으로 앞 2개 뒤 2개 중 가장 큰 건물을 찾자
        empty_list = [a, b, c, d]
        # print(empty_list)

        maxV = empty_list[0]
        for empty in empty_list:
            if maxV < empty:
                maxV = empty
        # print(maxV)

        if building[i+2] > maxV:   # 주변 건물보다 기준 건물이 큰 경우
            count += (building[i+2] - maxV)     # 그 차이가 조망권이 확보된 세대 수

    print(f'#{tc+1} {count}')
