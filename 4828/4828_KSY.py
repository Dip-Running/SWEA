T = int(input())    # 테스트 케이스의 갯수






for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_number = min(numbers)
    max_number = max(numbers)   
    print(f'#{i+1} {max_number - min_number}')