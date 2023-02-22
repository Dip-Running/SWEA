### Time out - 68초ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
import sys

sys.stdin = open('input.txt', 'r')

import time
#####
ST = time.time()
# ar : 간선 표시 행렬, q : queue, vs : visited
def bfs(ar, q, vs):
    print(f'#{tc}', end=' ')
    ans = []
    while q:
        for i in q:
            vs[i] = 1
        node = q.pop(0)
        vs[node] = 1
        for edg in range(1, len(ar)):
            # 1부터 len(ar)까지 node와 연결된 선이 있으면
            if ar[node][edg] and not vs[edg]:
                ar[node][edg] = 0
                for x in range(1, v + 1):
                    for y in range(1, v + 1):
                        if ar[y][x] == 1:
                            break
                    else:
                        if not vs[x]:
                            q.append(x)
                            vs[x] = 1

        ans.append(node)
        print(node, end=' ')
    print()
    pass


T = 10
for tc in range(1, T + 1):
    v, e = map(int, input().split())

    arr = [[0] * (v + 1) for _ in range(v + 1)]
    edge = list(map(int, input().split()))
    # 간선 표시
    for i in range(e):
        arr[edge[i * 2]][edge[2 * i + 1]] = 1


    start_node = []
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if arr[j][i] == 1:
                break
        else:
            start_node.append(i)
    # print(start_node)
    visited = [0] * (v + 1)
    bfs(arr, start_node, visited)
EN = time.time()
print(ST - EN)