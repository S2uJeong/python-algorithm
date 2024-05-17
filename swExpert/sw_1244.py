"""
- dfs로 경우의 수를 다 살펴보는데 가지치기가 필요
    - 뒷 쪽 숫자가 더 클 경우에만 교환
    - 교환 횟수에 따라 따로 리스트에 값을 저장하여 중복 방지
"""
def dfs(numbers, cnt):
    global result
    tmp = ''
    for number in numbers:
        tmp += number

    # result에 같은 cnt로 이미 있는 값이면 return 아니면 진행
    if int(tmp) in result[cnt]:
        return
    else :
        result[cnt].append(int(tmp))

    # cnt가 0이면 다음 없이 끝
    if cnt == 0:
        return

    # 이중 for문을 돌며 교환한다.
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(numbers, cnt-1) # 교환을 했으므로 cnt를 깎고 넣는다.
            numbers[i], numbers[j] = numbers[j], numbers[i] # 원상복구

T = int(input())
for t in range(1,T+1):
    num, cnt = input().split()
    result = [[] for _ in range(int(cnt)+1)]

    dfs(list(num), int(cnt))
    print(f'#{t} {max(result[0])}')