# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().strip()))
    c = [0] * 10    # count 배열 초기화
    for i in arr:
        c[i] += 1   # arr의 값에 해당하는 c의 인덱스 ++
    c.reverse() #순서 뒤집음
    # 카드 장수가 같을 때는 적힌 숫자가 큰쪽이 나오게 하기 위해
    Max = -1
    for i in range(10): # 같은 값 "초과"일 때만 값이 바뀌도록 설정
        if Max < c[i]:
            Max = c[i]
    # 역순으로 바꿨으므로 최댓값의 index를 에서 빼야함
    print(f'#{tc} {9 - c.index(Max)} {Max}')