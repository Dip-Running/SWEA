import sys
sys.stdin = open('input.txt','r')
T = 10
for tc in range(1, T + 1):
    n = int(input())        # 이동 허가 횟수
    arr = list(map(int, input().split()))   # 배열
    c = [0] * 1000       # 상자 높이는 1 이상 100 이하
    for i in arr:   # 인덱스는 상자의 높이 값, value는 높이 값의 갯수
        c[i] += 1
    for i in range(n+1):    # n 회니까 n+1만큼 돌려야함
        a = 0
        while c[a] == 0:    # a 올라감
            a += 1
        b = len(c)-1        # 제일 뒤 index number
        while c[b] == 0:    # b 내려감
            b -= 1
        c[a] -= 1   # a: -1, a+1: +1
        c[a+1] += 1
        c[b] -= 1   # b: -1, b-1: +1
        c[b-1] += 1
    print(f'#{tc} {abs(a - b)}')