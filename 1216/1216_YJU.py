for tt in range(1, 11):
    n = int(input())
    matrix = [input() for _ in range(100)]
    for i in range(100): # 세로줄 문자 넣기
        columns = []
        for j in range(100):
            columns.append(matrix[j][i])
        matrix.append(''.join(columns))
    want = []
    i = 100
    while i > 0:
        new = [alpha[k:k+i] for alpha in matrix for k in range(100-i+1) if alpha[k] == alpha[k+i-1]]    
        for c in new:
            c_list = list(c)
            j = i//2
            while j>0:
                left = c_list.pop(0)
                right = c_list.pop()
                if left != right:
                    break
                j -= 1
            if j == 0:
                want.append(c)
                break
        if want:
            break
        i -= 1
    print(f'#{tt} {len(want[0])}')