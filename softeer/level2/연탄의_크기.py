N = int(input())
nums = list(map(int,input().split()))

result = 0
for i in range(2, 101):
    tmp_result = 0
    for num in nums :
        if num % i == 0 :
            tmp_result += 1
    result = max(result, tmp_result)

print(result)