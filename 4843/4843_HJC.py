import sys
sys.stdin = open('input.txt', 'r')
#------------------------#
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(5):
        # ans에 더함 arr에서 빼서 arr의 max값의 인덱스가 들어있는 val을 빼서
        ans.append(arr.pop(arr.index(max(arr))))
        # ans에 더함 arr에서 빼서 arr의 min값의 인덱스가 들어있는 val을 빼서
        ans.append(arr.pop(arr.index(min(arr))))
    print(f'#{tc}', end=' ')
    print(*ans)