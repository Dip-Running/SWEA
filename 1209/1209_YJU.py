for tt in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    row, columns, trace_1, trace_2 = 0,0,0,0

    for idx, i in enumerate(board):
    
        if row < sum(i): # 행
            row = sum(i)
        trace_1 += i[idx] # 대각
        trace_2 += i[len(board)-1 - idx] # 대각
    
        column = 0
        for j in range(len(board)): # 열
            column += board[j][idx]
    
        if columns < column:
            columns = column
    print(f'#{tt} {max(row, columns, trace_1, trace_2)}')