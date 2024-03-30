def binary_serch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return "no"

N = int(input())
stocks = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))

# 1. 정렬한다.
stocks.sort()
# 2. 이진탐색 시작.
result = []
for order in orders:
    tmp = binary_serch(stocks, order, 0, len(stocks)-1)
    result.append(tmp)

print(result)