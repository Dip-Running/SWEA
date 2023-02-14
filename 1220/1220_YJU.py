for tt in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    new = [[] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new[i].append(matrix[j][i])
    result = 0
    for line in new:
        stack = []
        cnt = 0
        for i in line:
            if not stack and i == 1:
                stack.append(i)
                continue
            if stack and i == 2:
                stack.clear()
                cnt += 1
        result += cnt
    print(f'#{tt} {result}')