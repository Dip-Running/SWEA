dic = dict({
    'ZRO':0,
    'ONE':1,
    'TWO':2,
    'THR':3,
    'FOR':4,
    'FIV':5,
    'SIX':6,
    'SVN':7,
    'EGT':8,
    'NIN':9,
})
from collections import Counter
T = int(input())
for tt in range(1, T+1):
    t, n = input().split()
    num = list(input().split())
    num = Counter(num)
    result = []
    for i in dic.keys():
        for j in range(num[i]):
            result.append(i)
    print(t, *result)