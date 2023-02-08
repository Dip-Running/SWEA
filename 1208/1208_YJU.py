# 2일차 1208_Flatten
for tt in range(1,11):
    N = int(input()) # 덤프 횟수
    n = list(map(int, input().split()))

    i = 0
    while i < N:
        n[n.index(max(n))] -= 1
        n[n.index(min(n))] += 1

        if max(n) - min(n) <=1:
            break        
        i += 1
        
    print(f'#{tt} {max(n) - min(n)}')