T = 10  # 테스트 케이스 10개

for tc in range(T):
    n = int(input())  # 덤프 횟수
    numbers = list(map(int, input().split()))  # 상자의 높이값 리스트 형변환
    N = len(numbers)

    for _ in range(n):
        for i in range(N - 1, 0, -1):  # 각 구간의 끝
            for j in range(0, i):  # 비교할 왼쪽 원소
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

        # print(numbers) 일단 정렬
        numbers[-1] -= 1    # 젤 큰 값에서 하나 빼서
        numbers[0] += 1     # 젤 작은 값에 하나 더하기

    if numbers[-2] - numbers[1] <= 1:   # 차이가 1이하면 -> 정렬 전이므로 뒤에서 2번째에서 앞에서 두번째 비교해야됨
        print(f'#{tc+1} 1')

    else:   # 차이가 1이 아니라면 그냥 차이 구하기
        print(f'#{tc+1} {numbers[-2] - numbers[1]}')


