T = int(input())
for test_case in range(1, T+1):
    money = int(input())

    charge = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_list = [0] * 8

    for i in range(8):
        if money // charge[i] != 0:     # 나누어 떨어지지 않는다면
            money_list[i] = money // charge[i]  # 몫을 money_list에 넣어주고
            money = money % charge[i]   # money에 money를 charge로 나눈 나머지를 할당한다
    print(f'#{test_case}')
    print(*money_list)