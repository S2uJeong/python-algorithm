import sys

iterable_num = int(input())

input_list = list(map(int,[sys.stdin.readline().strip() for _ in range(iterable_num)]))

input_list.sort()
# input_list.sort(reverse=True) 내림차순 정렬
print(*input_list)