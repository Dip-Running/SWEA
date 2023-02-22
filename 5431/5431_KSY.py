import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    students, good_students = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))    # 과제를 제출한 학생의 번호
    # 과제를 제출하지 않은 학생의 번호를 오름차순으로 출력

    number = [i for i in range(1, students + 1)]   # 정수 배열
    # print(number)
    bad_student = []
    for i in range(len(number)):
        if number[i] not in numbers:    # 과제를 제출한 학생의 번호가 아니라면
            bad_student.append(number[i])   # 나쁜 학생 리스트에 추가

    print(f'#{test_case}', *bad_student)