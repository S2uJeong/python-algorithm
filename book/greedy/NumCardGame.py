row, col = map(int,input().split())

card = [0]*row

for i in range(row):
    card[i] = list(map(int, input().split()))

rowList = [] # 각 행의 가작 작은 값을 저장할 list

for i in range(row):
    card[i].sort()
    rowList.append(card[i][0])

answer = max(rowList)

print(answer)

# ===== 책 답안 ==========
row, col = map(int,input().split())

result = 0

for i in range(row):
    data = list(map(int, input().split()))
    # 현재 행에서 '가장 작은 수' 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 '가장 큰 수' 찾기
    result = max(result, min_value)

print(result)
