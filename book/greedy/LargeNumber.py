length, count, continuedCount = map(int, input().split())

numList = list(map(int, input().split()))

numList.sort()
answer = 0

for i in range((count // (continuedCount+1))):
    answer += (numList[length-1] * 3)
    answer += numList[length-2]

if count % 2 == 1:
    answer += numList[length-1]

print(answer)


# ===== 책 답안 ==========
# .sort 까진 방법이 같음

first = numList[length - 1] # 가장 큰 수
second = numList[length - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(continuedCount):
        if count == 0:
            break
        result += first
        count -= 1
    if count == 0:
        break
    result += second
    count -= 1

print(result)