leng, target = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
for i in range(len(nums)):
    print(i)
    sum = nums[i]
    if sum == target:
        cnt += 1
        print(f'nums[{i}] 값이 target과 같음!! cnt ={cnt}, sum = {sum}')
        continue
    for j in range(i+1, len(nums)):
        sum += nums[j]
        print(f'{i} - {j} = {sum}')
        if sum == target:
            cnt += 1
            print(f'cnt ={cnt}, sum = {sum}')
            break
        if sum > target:
            print(f'sum이 target 보다 커짐!! cnt ={cnt}, sum = {sum}')
            break
print(cnt)