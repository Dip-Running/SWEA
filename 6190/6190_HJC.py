import sys
sys.stdin = open('input.txt', 'r')
#-------------------------------#

def check(num):
    tmp = str(num)
    for k in range(len(tmp) - 1):
        if tmp[k] > tmp[k + 1]: # 한번이라도 k번째가 k+1번째보다 크면 바로 리턴 false
            return False
    return True # 단조거나 한자릿수면 리턴 True

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    size = len(arr)
    ans = -1    # 기본 값
    for i in range(size):
        for j in range(i+1, size):
            num = arr[i]*arr[j]
            # 단조 판단
            if check(num):
                ans = max(ans, num)
    print(f'#{tc} {ans}')