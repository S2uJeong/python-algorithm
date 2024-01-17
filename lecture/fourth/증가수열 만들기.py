from collections import deque

N = int(input()) # 들어오는 숫자의 개수
nums = list(map(int,input().split()))

lt, rt = 0, N-1
last = -1
tmp = []
res = ""
while lt <= rt:
    if nums[lt] > last :
        tmp.append((nums[lt],'L'))
    if nums[rt] > last :
        tmp.append((nums[rt],'R'))
    tmp.sort()
    # 둘다 안 크다.
    if len(tmp) == 0:
        break
    else :
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':   # 조건으로 이 알파벳을 사용할 아이디어 또한 감탄,,
            lt += 1
        else :
            rt -= 1
    tmp.clear()

print(len(res))
print(res)

# ======= 고민의 흔적,, 인덱스를 기준으로 옮기면서 하면 쉽게 되는걸,,
# 분기로 두 수를 그때마다 비교해서 수를 직접 뽑으려고 하니까 복잡해지고 구현이 안됨.
   # -> 예제에선 일단 크면 양쪽 다 담은 뒤에 비교 하고서 답으로 넣는 방법으로 구현해냄.

# 리스트의 앞수와 끝수를 비교한 뒤, 더 작은 쪽의 인덱스를 반환한다.
 # 문제 조건상 같으면 앞수를 우선으로 함.
def compare(arr):
    if arr[0] > arr[-1] :
        return -1
    else :
        return 0

def fail():
    inc_nums = [-1]
    res = 0
    res_way = []
    while nums :
        ln = nums[0]
        rn = nums[-1]
        if len(nums) == 1:
            if nums[0] > inc_nums[-1]:
                res += 1
                res_way.append('L')
            else :
                nums.pop()
                break
        if ln <= inc_nums[-1] and rn <= inc_nums[-1]:
           nums.pop()
           nums.popleft()
           break
        if ln > inc_nums[-1] and rn > inc_nums[-1]:
            # copare로 값을 이분화 시켜, pop이 한 회전에 두 번 일어나 index out 나는 것을 방지한다.
            cp = compare(nums)
            if cp == 0 : # 왼쪽이 더 작다.
                res += 1
                inc_nums.append(nums.popleft())
                res_way.append('L')
                break
            if cp == -1 :
                res += 1
                inc_nums.append(nums.pop())
                res_way.append('R')
                break
        if ln > inc_nums[-1] or rn > inc_nums[-1]:
            cp = compare(nums)
            if cp == 0 :
                inc_nums.append(nums.pop())
                res += 1
                res_way.append('R')
            if cp == 1:
                inc_nums.append(nums.popleft())
                res += 1
                res_way.append('L')






