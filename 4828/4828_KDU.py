def maxx(lst):
    max_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if max_v < i:  # 큰값 만나면 값을 바꿈
            max_v = i
    return max_v

def minn(lst):
    min_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if min_v > i:  # 작은값 만나면 값을 바꿈
            min_v = i
    return min_v

T = int(input())

for tc in range(1, T+1):
    len_lst = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {maxx(lst) - minn(lst)}')