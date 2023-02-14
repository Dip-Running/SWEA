for tt in range(1):
    v, e = map(int, input().split())
    line = list(map(int, input().split()))
    result = []
    start = []
    end = []
    for i in range(len(line)):
        if not i % 2 :
            start.append(line[i])
        else:
            end.append(line[i])
    start_dic = dict()
    end_dic = dict()
    for i in range(1, v+1):
        start_dic.setdefault(i, [])
        end_dic.setdefault(i, [])
    for i, j in zip(start, end):
        start_dic[i].append(j) # key 출발 / value 도착
        end_dic[j].append(i) # key 도착 / value : key로 향하는 출발지
    # 어디서 출발해야하는지 모르기 때문에 end_dic를 확인하여 value가 비어있다면 작업을 시작할 수 있다고 판단함.
    while end_dic:
        for i, j in list(end_dic.items()):
            if not j: # 만약 value가 비어있다면 key에서 시작할 수 있는 곳이므로
                result.append(i) # result에 key를 추가
                for k in start_dic[i]: # start_dic에서 key가 갈 수 있는 곳을 탐색
                    end_dic[k].remove(i) # key에서 갈 수 있는 곳을 end_dic에서 지움
                end_dic.pop(i) # result에 append된 key는 이미 지나갔으므로 end_dic에서 key값까지 지워줌
    print(f'#{tt}', *result)