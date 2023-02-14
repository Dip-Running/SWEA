T = int(input())
for tt in range(1, T+1):
    N = int(input())
    cards = [int(i) for i in input()]

    cards_list = [0] * 10

    for i in cards:
        cards_list[i] += 1
    
    cnt = cards_list.count(max(cards_list))
    
    if cnt == 1:
        print(f'#{tt} {cards_list.index(max(cards_list))} {max(cards_list)}')
    
    else:
        for _ in range(cnt-1):
            cards_list.remove(max(cards_list))
        print(f'#{tt} {cards_list.index(max(cards_list)) + cnt -1} {max(cards_list)}')