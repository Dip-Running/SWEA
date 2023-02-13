import sys
sys.stdin = open('input.txt', 'r')
#-----------------------------#
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    Aarr = list(map(int, input().split()))
    Barr = list(map(int, input().split()))

    if a > b:   # a 사이즈가 더 크면 a와 b 바꿈
        a, b = b, a
        Aarr, Barr = Barr, Aarr

    ans = 0
    for i in range(b - a + 1):  # b 안에서 a가 돌 수 있는 만큼 반복
        _sum = 0
        for j in range(a):  # a 사이즈 만큼 반복
            # _sum에 각 인덱스 값 곱해서 더함
            _sum += Aarr[j] * Barr[i+j]
        ans = max(ans, _sum)    # 최댓값 비교

    print(f'#{tc} {ans}')