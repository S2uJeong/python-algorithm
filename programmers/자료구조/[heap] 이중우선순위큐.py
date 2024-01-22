# 예외처리
# 1. 빈 큐에 삭제 연산이 주어지면 연산을 무시한다.
# 2. 최종적으로 반환할 때, 큐가 비어 있으면 [0,0]으로 반환한다.
import heapq
def solution(operations):
    heap = []
    for op in operations:
        c, num = op.split()
        num = int(num)

        if c == 'I':
            heapq.heappush(heap, num)
        elif c == 'D' and num == 1:
            if len(heap) != 0:
                max_val = max(heap)
                heap.remove(max_val)
        else:
            if len(heap) != 0:
                heapq.heappop(heap)

    if len(heap) > 0:
        return [max(heap), min(heap)]
    else:
        return [0,0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
