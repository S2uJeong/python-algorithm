"""
두 용액을 합친 속성 값이 0에 가깝게 하는 두 용액을 출력.
해당 하는 것이 두개 이상이면, 아무거나 출력

용액의 종류 : 2 ~ 2_000_000_000
1초 안에 풀어야하므로 O(N) 미만의 로그 시간복잡도로 풀어야 한다.
로그 시간 복잡도 알고리즘 -> 이진탐색, 우선순위 큐


# 성공
-100000 ~ 100000 식으로 (오름차순) 정렬한 뒤,
양쪽 투포인터로 더한 값을 update 하고, 만약 양의 수가 나오면 + 의 수가 더 크다는 것이니 오른쪽 포인터를 1 줄인다
                                    음의 수가 나오면 - 의 수가 더 크다는 것이니 왼쪽 포인터를 1 늘린다.
                                    0 의 수가 나오면 반환하고 종료 한다. (아무거나 내보내도 되기 때문)
    -> 언제까지? 서로 같은 수를 집기 전까지.
    -> 인덱스 값을 update 할 때마다, result와 수를 비교한 뒤, result_liquids 배열을 초기화 해준다.
    🔴최대 값을 잘못 설정해서 실패 뜬거 확인 늦음

# 시간 초과
- 투 포인터 사용해서, 왼쪽을 기준으로 쭉 진행 하고, 오른쪽에서 왼쪽 기준까지 도달하기 까지의 용액을 하나하나 다 비교해준다.
- 이중 for문과 비슷한 모양이지만, 수를 진행할 수록 탐색할 용액의 수가 줄어들어 시간 안에 할 수 있다.
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
liquids = list(map(int,input().split()))
liquids.sort() # logN

def use_binary(N, liquids):
    result = int(1e10) # 🔴최대 값을 잘못 설정했었음 1e9로
    result_liquids = []
    left,right = 0, N-1
    while left < right:
        new_liquid = liquids[left] + liquids[right]
        # 정답 업데이트
        if abs(new_liquid) < result :
            result = abs(new_liquid)
            result_liquids = [liquids[left], liquids[right]] # 오름차순 출력
        # 가지 치기
        if new_liquid == 0 :
            break
        # 탐색 범위 줄이기
        elif new_liquid > 0 :
            right -= 1
        else :
            left += 1

    for l in result_liquids:
        print(l, end=' ')

def use_for_timeout(N, liquids):
    result = int(1e9)
    result_liquids = []
    for left in range(len(liquids)):
        for right in range(len(liquids)-1, left,-1):
            new_liquid = liquids[left] + liquids[right]
            if new_liquid == 0 :
                print(liquids[left], liquids[right])
                exit()
            if abs(new_liquid) < result :
                result = abs(new_liquid)
                result_liquids = [liquids[left], liquids[right]]

    for l in result_liquids:
        print(l, end=' ')


use_binary(N,liquids)