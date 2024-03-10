import heapq

# 매 홀수째 인덱스까지의 리스트를 넣었을 때 중앙 값을 계산할 함수
def calculate(iterable):
    h = []
    # print(f'calculate 매개변수 : {iterable}')
    for val in iterable:
        heapq.heappush(h,val)

    idx = len(iterable)//2
    for i in range(len(h)):
        if i == idx:
            return heapq.heappop(h)
        heapq.heappop(h)
    return None

# 조건에 맞는 print법
def print_num(iterable):
    # 1. 총 갯수 출력
    print(len(iterable))
    # 2. 원소 출력
    cnt = 0 # 10번째 출력인지 확인할 변수
    for i in range(len(iterable)):
        if cnt == 10 :
            print()
            cnt = 0
        cnt += 1
        print(iterable[i], end=' ')

T = int(input())
for _ in range(T):
    n = int(input())
    # 입력 받을 시 조건에 맞게
    if n > 10 :
        forn = round(n / 10 + 0.5)
        nums = []
        for i in range(forn):
            nums += list(map(int,input().split()))
    else :
        nums = list(map(int,input().split()))

    result_list = []

    for i in range(len(nums)):
        if i % 2 == 0 :
            result_list.append(calculate(nums[0:i+1]))
    print_num(result_list)
