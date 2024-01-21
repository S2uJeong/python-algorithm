N = int(input())
arr = list(map(int, input().split()))
res = [0] * N

for num, cnt in enumerate(arr):  # 숫자 : num +1, cnt : 역수의 개수
    for idx, val in enumerate(res):
        if cnt == 0 and val == 0:
            res[idx] = num + 1
            break
        elif val == 0:
            cnt -= 1
print(res)