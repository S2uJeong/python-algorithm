import sys

input = sys.stdin.readline

# ==== 순차탐색으로 만든 것. =======
def cut(stocks, request):
    longest_stock = max(stocks)
    remains = 0
    result = False

    while not result:
        longest_stock -= 1

        if remains >= request:
            result = True
            return longest_stock

        for stock in stocks:
            if stock <= longest_stock:
                continue
            else:
                remains += stock - longest_stock


# ===== 이진탐색 활용 =======
def binary_cut(stocks, request):

    result = 0
    start, end = 0, max(stocks)
    mid = (start + end) // 2

    while start <= end:
        # 🔴 오답노트
        remains = 0
        mid = (start + end) // 2

        for stock in stocks:
            if stock > mid:
                remains += (stock - mid)
        if remains < request:
            end = mid - 1
        else:
            start = mid + 1
            # 🔴 이 부분을 이해하는게 중요 (최적화)
            result = mid

    return result


# ==== 결과 출력 =====
m, request = map(int, input().split())
stocks = list(map(int, input().split()))

print(cut(stocks, request))
print(binary_cut(stocks, request))
