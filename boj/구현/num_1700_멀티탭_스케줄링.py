"""
플러그 수만큼 길이를 가진 배열 생성
배열에 입력 순서대로 넣고, 꽉 차면 아래 if문으로
    - 현재 플러그 배열에, 현재 포인터인 입력 배열의 값 포함 플러그 길이 만큼의 idx 안에 존재하면 그 값은 플러그에서 제외 하지 않거나, 최대한 뒤에 있는것을 뽑는다.
        - 만약 같은 수가 연달아 나오면 그건 continue 해준다.
    - 끝까지 값이 존재하지 않으면 그냥 바로 다음값을

try-except를 사용해서 푸는 방법을 익혀야함.
belady's min algorithm
"""
n,l = map(int,input().split())
nums = list(map(int,input().split()))

cnt = 0
plug = set()
def find_latest(idx):
    result = 0
    max_idx = -1
    for num in plug:
        try:
            num_idx = nums[idx:].index(num)
        except:
            num_idx = l
        if max_idx < num_idx:
            result, max_idx = num, num_idx

    return result


for idx, num in enumerate(nums):
    plug.add(num)
    if len(plug) > n:
        cnt += 1
        latest_used = find_latest(idx)
        plug.discard(latest_used)

print(cnt)
