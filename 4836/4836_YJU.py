T = int(input())
for tt in range(1, T+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    board = [[0]* 10 for _ in range(10)]

    for k in box:
        for j in range(k[1], k[3]+1):
            for l in range(k[0], k[2] +1):
                board[j][l] += k[4]
    
    board = sum(board,[])
    cnt = 0
    for i in board:
        if i == 3:
            cnt += 1
    print(f'#{tt} {cnt}')
