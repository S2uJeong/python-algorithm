"""
- 시간복잡도 : O(nlogn)
- 내림차순 - 최소힙, 오름차순 - 최대힙
- 최대힙 : 부모노드가 자식노드보다 큰 트리
"""
import heapq

def use(iterable) :
    # 1.생성 - heapq.heapify() : 제자리에서 heap으로 만들어 준다.
    heapq.heapify(iterable)
    # 2.추가 - heapq.heappush(heap, item) : 힙이 깨지지 않게 push
    heapq.heappush(iterable, 10)
    # 3. 제거 - heapq.heappop() : 최대힙은 제일 작은수를, 최소힙은 제일 큰수를 뽑아낸다.
    heapq.heappop(iterable)
    # 출력방법 - print(list(heapq)) 이렇게 출력 안된다.
    # return [val for val in iterable] 이것도 오답
    return [heapq.heappop(iterable) for _ in range(len(iterable))]
def heapsort(iterable):
    # 1. haep자료구조로 쓸 list를 선언한다.
    h = []
    # 2. heappush - 대상인 iterable 자료에서 값을 하나씩 넣어준다.
    for value in iterable:
        heapq.heappush(h,value)
    # 3. heappop - 힙에서 값을 하나씩 pop하여 return한다.
    result = [heapq.heappop(h) for i in range(len(h))]
    print(f'result = {result}')
    print(f'h = {h}') # 3-1. pop은 값을 빼는것이기 때문에 h는 빈 리스트가 된다.
    return result

# 힙 정렬 함수 이용
print(heapsort([1,3,6,1,3,6,74,5,23]))
print(use([1,4,2,3,50,2,0,9]))