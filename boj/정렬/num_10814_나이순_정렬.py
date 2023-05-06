import sys
input = sys.stdin.readline

n = int(input())

list = []

for _ in range(n):
    age, name = input().split()

    list.append([int(age),name])

list.sort(key= lambda x : (x[0]))

for i in range(n):
    print(list[i][0], list[i][1])