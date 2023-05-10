# 카드의 개수는 100,000개가 최대
# 카드에 적혀 있는 숫자는 범위가 넓음
# 계수 정렬은 메모리 초과 될 듯함.

import sys
input = sys.stdin.readline

n = int(input())
list = []
count_dic = {}

for _ in range(n) :
    list.append(int(input().strip()))

for num in list:
    if num in count_dic.keys():
        count_dic[num] += 1
    else:
        count_dic[num] = 1

result = sorted(count_dic.items(), key = lambda x: (-x[1],x[0]))

# print(type(result))

print(result[0][0])
