import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        tmp = heapq.heappop(scoville) # 제일 지수가 작은 음식
        if tmp >= K: # 만약 리스트 안의 제일 지수가 작은 음식이 k보다 크거나 같다면 return answer
            return answer
        else:
            tmp = tmp + (heapq.heappop(scoville) *2) # 제일 지수가 작은 음식 + 두번째로 작은 음식
            heapq.heappush(scoville,tmp) # 더한 값을 넣는다.
            answer += 1
    if heapq.heappop(scoville) >= K:
        return answer
    else :
        return -1

print(solution([1,2,3,9,10,12], 7))