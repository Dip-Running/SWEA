# import sys
# sys.stdin = open('input.txt','r')
#-------------------------#
import sys

T = 10
for tc in range(1, T + 1):
    size = 8
    m = int(input())
    lst = [list(map(str, input())) for _ in range(size)]
    cnt = 0
    for i in range(size):
        for j in range(size - m + 1):
            posSt = j
            posEn = m + j
            word = lst[i][posSt:posEn]
            if word == word[::-1]:
                cnt += 1

    for i in range(size):
        for j in range(size - m + 1):
            word = ''
            for k in range(m):
                word += lst[j + k][i]
            if word == word[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')