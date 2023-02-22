# import sys
# sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    subject, select = map(int, input().split())
    scores = list(map(int, input().split()))

    sorted_scores = sorted(scores, reverse=True)  # 점수 정렬(오름차순)
    total = 0   # 성적의 합계 구하기
    for i in range(select):
        total += sorted_scores[i]

    print(f'#{test_case}', total)