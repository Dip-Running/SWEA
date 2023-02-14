# 문자열에서 (리스트도 가능) 가장 많은 요소가 무엇인고 몇 개인지 구하기
T = int(input())    # 테스트 개수

for i in range(T):      # 테스트 개수만큼 반복
    N = int(input())        # 카드 개수
    numbers = str(input())  # 카드 입력

    count_list = [0]*10     # count sms 0부터 9까지 받을 수 있다(카드의 숫자 번호 개수) 
    for j in numbers:       # 카드 문자열에 있는 j 반복
        count_list[int(j)] += 1     # j 인덱스에 1씩 추가

    max_count = max(count_list)     # 가장 많은 숫자의 개수는 count_list에서 가장 큰 수이다

    for k in range(len(count_list)):    # k 를 count_list의 개수만큼 반복
        if max_count == count_list[k]:  # 가장 많은 숫자의 개수와 count_list의 k 번째 요소와 같다면
            max_number = k              # k 가 가장 많은 숫자

    print(f'#{i+1} {max_number} {max_count}')
    

    
    
