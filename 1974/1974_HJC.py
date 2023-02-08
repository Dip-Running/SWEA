T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cnt = sum_box = sum_x = sum_y = 0
    for i in range(0, 9):
        for j in range(0, 9):
            sum_x += arr[i][j]  # x축 확인
            sum_y += arr[j][i]  # y축 확인
        if sum_x != sum_y != 45:
            cnt += 1

    for i in range(0, 3):
        for j in range(0, 3):
            for l in range(0, 3):
                for k in range(0, 3):
                    sum_box += arr[3*i+l][3*j+k]
            if sum_box != 45:
                cnt += 1
            sum_box = 0
    if cnt == 0:
        print(f"#{test_case}", "1")
    else:
        print(f"#{test_case}", "0")
