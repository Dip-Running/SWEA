T = int(input())
for tt in range(1,T+1):
    n = int(input())
    num = list(map(int, input().split()))
    print(f'#{tt}', end = ' ')
    i = 0
    while i<10:
        if i%2 == 0:
            print(num.pop(num.index(max(num))), end = ' ')
            i += 1
        else:
            print(num.pop(num.index(min(num))), end = ' ')
            i += 1
    print()