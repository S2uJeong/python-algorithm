import sys

input = sys.stdin.readline
#
# total_num = int(input())
#
# list = []
#
# for _ in range(total_num):
#     x,y = map(int,input().split())
#
#     list.append([x,y])
#
# list.sort(key = lambda x : (x[0],x[1]))
#
# for i in range(total_num):
#     print(list[i][0], list[i][1])


for p in sorted([tuple(map(int,input().split())) for _ in range(int(input()))]):
    print(p[0], p[1])



