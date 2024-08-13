"""
N개의 정수로 이루어진 배열 A

수열의 길이가 8까지로 짧으므로 dfs를 이용해서 풀이
"""
def calculate(list):
    sum = 0
    for i in range(len(list)-1):
        sum += abs(list[i] - list[i+1])
    return sum

def dfs(crt_list,num_dicts):
    global result
    if len(crt_list) >= N:
        result = max(result, calculate(crt_list))
        return

    for num in num_dicts:   # 🔴 not in 으로 조건걸어서 했다가, 같은 숫자가 또 들어올 수 있는 수열이란것을 간과해서 틀림. 따라서 dict 으로 갯수를 세서 로직 구성 (ex:[3,1,3,1])
        if num_dicts[num] > 0 :
            num_dicts[num] -= 1
            crt_list.append(num)
            # print(f'dfs({crt_list},{num_dicts})')
            dfs(crt_list,num_dicts)
            crt_list.pop()
            num_dicts[num] += 1


N = int(input())
nums = list(map(int,input().split()))

num_dicts = {}
for num in nums:
    if num in num_dicts:
        num_dicts[num] += 1
    else:
        num_dicts[num] = 1

result = 0
dfs([],num_dicts)
print(result)