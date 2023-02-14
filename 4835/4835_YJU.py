T = int(input())
for tt in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    result = []
    
    for i in range(n-m+1):
        result.append(sum(num[i:i+m]))
    
    print(f'#{tt} {max(result) - min(result)}')