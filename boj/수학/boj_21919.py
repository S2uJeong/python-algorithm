"""
1. 소수인지 아닌지 판별하는 함수
  - 리스트 탐색하며 해당 함수 실행 시키고, True면 new_arr에 담는다.
2. "최소"공배수니까 소수들 중 제일 큰 숫자를 기준으로 탐색한다.
  - if new_arr의 길이가 0 이면 answer = -1 end
"""

N = int(input())
inputs = list(map(int,input().split()))
inputs = set(inputs) # 소수인데 같은 수인 경우 방지

# 1. 소수 리스트 생성
# 들어오는 숫자의 범위는 2 ~ 1,000,000 / idx : 숫자, val : 소수인지 아닌지
prime_list = [True] * 1000001
prime_list[0] = False
prime_list[1] = False
for num in range(2,5001):
    if prime_list[num] == True:
        for j in range(num*2, 1000001, num):
            prime_list[j] = False

# 2. 문제 풀이
answer = 1
for num in inputs:
    if prime_list[num]:
        answer *= num

# 3. 출력
if answer == 1:
    print(-1)
else:
    print(answer)


