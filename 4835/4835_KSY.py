T = int(input())    # 테스트 개수


for i in range(T):
    N, M = map(int, input().split())    # N : 정수의 개수 # M: 구간의 개수
    numbers = sorted(list(map(int, input().split())))
# print(numbers)
    min_sum = sum(numbers[:M])
    max_sum = sum(numbers[-M:])
    sub_sum = max_sum - min_sum
    print(f'#{i+1} {sub_sum}')
    
