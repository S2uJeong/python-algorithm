"""
K번 삭제하여 짝수로 이루어진 연속한 부분 수열 중, 가장 긴 길이를 구하라

수열의 길이 : 1 ~ 50,000 / 삭제 횟수 : 1 ~ 100 / 제한시간 1초

1. 투포인터로 부분 수열을 지정
2. 투 포인터 사이에 홀수의 갯수가 K개 초과면 L증가, 반대는 R을 증가시킨다.

🔴 처음에 이중 for문으로 매번 부분수열의 처음부터 끝까지 갯수를 다시 세어 주는 로직은 시간초과가 났음
수열문제고, 방향이 한쪽으로 진행되므로 while 하나로 이전에 쓰던 count를 활용해서 오른쪽으로 진행하게 했더니 시간내에 풀림
"""

"""
# 실패 Ver
start = 0
end = 1
flag = True
result = 0

while True and flag:
    cnt = 0
    size = 0
    for idx in range(start, end+1):
        if idx >= N :
            flag = False
            break
        else :
            if nums[idx] % 2 == 1 :
                cnt += 1
            else :
                size += 1

    if cnt > K :
        start += 1
    else :
        result = max(size, result)
        end += 1

"""


N,K = map(int,input().split())
nums = list(map(int,input().split()))

start,end = 0,0
cnt = 0
result = 0
while end >= start:
    # end 기점을 기준으로 매순간 홀수인지 짝수인지 점검
    if nums[end] % 2 == 1:
        cnt += 1

    # 만약 홀수 수가 K보다 많으면 start를 늘려준다.
    if cnt > K:
        if nums[start] % 2 == 1:
            cnt -= 1
        start += 1

    else:
        result = max(result, (end - start + 1) - cnt)

    end += 1
    if end >= N:
        break

print(result)