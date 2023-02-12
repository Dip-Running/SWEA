import sys
sys.stdin = open('input.txt', 'r')
def check(arr, M):  # 회문 확인 함수 input : 전체 arr, M : 회문 판별할 길이
    for lst in arr: # 한줄씩 읽음
        # 100 - 판별 길이 + 1 = 한줄에 판별 길이가 몇개 나오는지 알 수 있음
        for j in range(N - M + 1):
            # 한 줄당 j부터 j + M까지 슬라이싱, 역순과 비교
            if lst[j:j+M] == lst[j:j+M][::-1]:
                return M # 한 번이라도 같으면 해당 판별길이 리턴
    return 1 # arr 다돌아도 회문이 없으면 1 리턴(최소 회문 길이)
T = 10
N = 100
for tc in range(1, T + 1):
    _ = int(input())    # 안쓰는 변수
    ans = 0
    arr = [list(input()) for _ in range(N)]
    _arr = list(zip(*arr))
    for i in range(N):
        M = i   # 회문 판별 길이
        # 해당 arr에서 회문의 길이가 최대인 값을 찾아야 하기 때문에 0부터 100까지 다 넣어봄
        ans = max(check(arr, M), check(_arr, M), ans)
    print(f'#{tc} {ans}')
