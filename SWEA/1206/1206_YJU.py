for tt in range(1, 11):
    num = int(input())
    N = list(map(int, input().split()))
    ans = 0

    for k in range(2, num-2):
        result = []
        result += N[k-2:k+3]
        for i in range(1, len(result)):
            for j in range(i, 0, - 1):
                if result[j - 1] > result[j]:
                    result[j - 1], result[j] = result[j], result[j - 1]
        if result[-1] == N[k]:
            ans += (result[-1]- result[-2])

    print(f'#{tt} {ans}')