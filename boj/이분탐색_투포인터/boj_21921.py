"""
(len - 기간) idx 이전까지 기간만큼을 더해서 해당 idx에 저장 하고 제일 큰 값 찾기
  - 만약 제일 큰 값이 0 이면 SAD
"""
N, X = map(int,input().split())
visitors = list(map(int,input().split()))

memo = [0] * N
result = 0
cnt = 0
i, j = 0, X
while j <= N : # 끝 부분인 j가 리스트의 범위를 넘지 않을 떄 까지
    tmp = memo[i] - visitors[i-1] + visitors[j-1]
    if tmp > result :
        cnt = 1 # 지금 값을 기준으로 셀거기 때문에 cnt 초기화
        result = tmp
    elif tmp == result: # 현재 기준 최대값과 같다면 cnt만 늘려준다.
        cnt += 1
    i += 1
    j += 1

# 결과 출력
if result == 0 :
    print("SAD")
else :
    print(result)
    print(cnt)

def fail_time(N,X,visitors):
    result = 0
    cnt = 0
    i, j = 0, X
    while j <= N : # 끝 부분인 j가 리스트의 범위를 넘지 않을 떄 까지
        tmp = sum(visitors[i:j])
        if tmp > result :
            cnt = 1 # 지금 값을 기준으로 셀거기 때문에 cnt 초기화
            result = tmp
        elif tmp == result: # 현재 기준 최대값과 같다면 cnt만 늘려준다.
            cnt += 1
        i += 1
        j += 1

    # 결과 출력
    if result == 0 :
        print("SAD")
    else :
        print(result)
        print(cnt)



