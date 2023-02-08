# import sys
# sys.stdin = open('input.txt', 'r')

for _ in range(1, 11):
    test_case = int(input())
    # 100 * 100 2차원 리스트 입력
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 1차원 리스트 사이즈 202로 초기화
    Sum = list(0 for i in range(0, 202))

    for i in range(0, 100):
        for j in range(0, 100):
            # 가로 합
            Sum[i] += arr[i][j]
            # 세로 합
            Sum[100+i] += arr[j][i]
        # 왼쪽 위부터 오른쪽 아래까지 합
        Sum[200] += arr[i][i]
        # 오른쪽 위부터 왼쪽 아래까지 합
        Sum[201] += arr[i][99 - i]

    print(f"#{test_case}", max(Sum))