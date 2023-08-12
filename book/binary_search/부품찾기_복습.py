import sys
# 입력 받기
input = sys.stdin.readline

stock_num = int(input().rstrip())
stock_list = list(map(int,input().split()))
order_num = int(input().rstrip())
order_list = list(map(int,input().split()))

# 이진탐색 함수 정의
def binary_search(list, target, start, end):
    while start <= end :
        mid = (start + end) // 2
        if list[mid] == target:
            return 1
        elif list[mid] < target:
            start = mid + 1
        else :
            end = mid - 1

    return 0

# 문제 해결
stock_list.sort()
result = []
for order in order_list:
    if binary_search(stock_list, order, 0, stock_num-1) == 0 :
        result.append("no")
    else :
        result.append("yes")

print(*result)