'''
p.311
'''
n = int(input())
nums = list(map(int,input().split()))

nums.sort() # 작은 수 부터 그 수대로 그룹을 만들면, 그룹의 수가 최대가 된다.
result = 0 # 그룹 수
cnt = 0 # 고용된 모험가의 수

for num in nums :
    cnt += num
    if cnt >= len(nums):
        break
    result += 1

print(result)
