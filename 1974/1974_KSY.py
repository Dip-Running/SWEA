# import sys
# sys.stdin = open('input.txt')
T = int(input())    # 테스트 케이스의 개수

for tc in range(1, T+1):
    row_sudoku = [list(map(int, input().split())) for _ in range(9)]     # 스도쿠를 2차원 리스트로 입력 받음
    col_sudoku = [[0] * 9 for _ in range(9)]
    # 세로 줄 이차원 리스트 받기
    for i in range(9):
        for j in range(9):
            col_sudoku[i][j] = row_sudoku[j][i]

    # 탐색
    result = 1
    for i in range(9):
        for j in range(1, 10):
            # 가로 줄 개수가 1개씩인지 확인
            if row_sudoku[i].count(j) != 1:
                result = 0
                break
            # 세로 줄 개수가 1개씩인지 확인
            if col_sudoku[i].count(j) != 1:
                result = 0


    # 3 X 3 탐색
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                sudoku_list = []
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        sudoku_list.append(row_sudoku[p][q])

                if sorted(sudoku_list) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    result = 0
    print(f'#{tc} {result}')

