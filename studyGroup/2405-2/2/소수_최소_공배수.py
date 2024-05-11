"""
1. 소수인지 아닌지 판별하는 함수
  - 리스트 탐색하며 해당 함수 실행 시키고, True면 new_arr에 담는다.
2. "최소"공배수니까 소수들 중 제일 큰 숫자를 기준으로 탐색한다.
  - if new_arr의 길이가 0 이면 answer = -1 end
"""

N = int(input())
inputs = list(map(int,input().split()))

# 1. 소수 리스트 생성
# 들어오는 숫자의 범위는 2 ~ 1,000,000 / idx : 숫자, val : 소수인지 아닌지
prime_list = [True] * 1000001
prime_list[0] = False
prime_list[1] = False
for num in range(2,5001):
    if prime_list[num] == True:
        i = 1
        while True:
            i += 1
            if num * i > 1000000 :
                break
            prime_list[num*i] = False

# 2. 주어진 값들 중 소수인것만 담기
new_nums = []
for num in inputs:
    if prime_list[num]:
        new_nums.append(num)

def solution(new_nums) :
    if len(new_nums) == 0 :
        return -1
    # 최소공배수는 소수 리스트를 다 곱한것을 기본으로 시작한다.
    tmp = 1
    for num in new_nums:
        tmp *= num
    # 소수들 중 가장 큰 값의 배수를 기준으로 해당 값을 모든 소수들이 만들 수 있는지 확인한다.
    max_val = max(new_nums)
    answer = tmp
        # 확인은 기본 최소공배수 값까지만 진행한다.
    for i in range(max_val, tmp+1, max_val):
        flag = True  # 최소공배수 될 수 있나?
        for num in new_nums:
            if i % num == 0:
                continue
            else :
                flag = False
                break
        if flag == True:
            if i < answer :
                answer = i
    return answer

print(solution(new_nums))


