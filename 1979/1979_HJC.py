# import sys
# sys.stdin = open('input.txt', 'r')
#------------------------#
# 입력받은 배열에 행과 열을 1씩 추가하고, 0 이 나온 지점부터 다음 0까지 길이 비교

def counter(arr):
    # print()
    ans = 0
    for i in arr:
        cnt = 0
        for j in i:
            if j:       # 1이면 cnt += 1
                cnt += 1
            # 0이면 현재까지의 cnt 가 m과 같은지 비교, 일치하면 ans += 1
            else:
                if cnt == M:
                    ans += 1
                cnt = 0
        #     print(cnt, end=' ')
        # print()
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]+[[0] * (N + 1)]
    _arr = list(zip(*arr))

    ans = counter(arr) + counter(_arr)
    print(f'#{tc} {ans}')