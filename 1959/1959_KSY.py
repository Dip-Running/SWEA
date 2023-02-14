T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # A의 개수, B의 개수
    numbers_A = list(map(int, input().split()))
    numbers_B = list(map(int, input().split()))

    # 길이가 더 긴 걸 B에 주기
    if len(numbers_B) < len(numbers_A):
        numbers_B, numbers_A = numbers_A, numbers_B

    n = len(numbers_A)
    m = len(numbers_B)

    # 곱하기 구하기
    multiple_list = [0] * (m-n+1)
    for j in range(m-n+1):
        for i in range(n):
            # print(numbers_A[i] * numbers_B[i+j])
            multiple_list[j] += (numbers_A[i] * numbers_B[i+j])
    # print(multiple_list)

    '''
    a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    a[0]*b[1] + a[1]*b[2] + a[2]*b[3]
    a[0]*b[2] + a[1]*b[3] + a[2]*b[4]
    '''
    # 최댓값 구하기
    maxV = multiple_list[0]
    for i in range(1, m-n+1):
        if maxV < multiple_list[i]:
            maxV = multiple_list[i]

    # 출력
    print(f'#{test_case} {maxV}')
