import sys
sys.stdin = open('input.txt', 'r')
#------------------------#
def StrToInt(word):
    if word == 'ZRO':
        ansNum.append(0)
    elif word == 'ONE':
        ansNum.append(1)
    elif word == 'TWO':
        ansNum.append(2)
    elif word == 'THR':
        ansNum.append(3)
    elif word == 'FOR':
        ansNum.append(4)
    elif word == 'FIV':
        ansNum.append(5)
    elif word == 'SIX':
        ansNum.append(6)
    elif word == 'SVN':
        ansNum.append(7)
    elif word == 'EGT':
        ansNum.append(8)
    elif word == 'NIN':
        ansNum.append(9)

def IntToStr():
    for i in ansNum:
        if i == 0:
            ans.append('ZRO')
        elif i == 1:
            ans.append('ONE')
        elif i == 2:
            ans.append('TWO')
        elif i == 3:
            ans.append('THR')
        elif i == 4:
            ans.append('FOR')
        elif i == 5:
            ans.append('FIV')
        elif i == 6:
            ans.append('SIX')
        elif i == 7:
            ans.append('SVN')
        elif i == 8:
            ans.append('EGT')
        elif i == 9:
            ans.append('NIN')

T = int(input())
for tc in range(1, T + 1):
    ansNum = []
    ans = []
    testcase = list(map(str, input()))
    arr = list(map(str, input().split()))
    for i in arr:
        StrToInt(i)
    ansNum.sort()
    IntToStr()

    print(f'#{tc} {" ".join(ans)}')