import sys
input = sys.stdin.readline

total_num = int(input())

list = []

for _ in range(total_num):
    x,y = map(int,input().split())

    list.append([x,y])

list.sort(key = lambda x : (x[1],x[0]))

for i in range(total_num):
    print(list[i][0], list[i][1])

# print(type(list[0][0]))