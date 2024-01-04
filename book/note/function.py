def test(num):
    print("It is Test")
    return num**2

print(test(2))
print('\n')
test(2)
print('\n')
print('람다식 활용:')
def add(a,b):
    return a + b
print(add(3,7))

print((lambda a,b : a + b)(3,7))

# Heapq 활용하기 - 정렬
import heapq
def heapsort(iterable):
    hlist = []
    result = []
    # 모든 원소를 힙에 삽입
    for x in iterable:
        heapq.heappush(hlist,x)
        # heapq.heappush(hlist,-x)   # 내림차순
    # 힙에 담긴 모든 원소를 꺼내어서 결과 변수에 넣기
    for i in range(len(hlist)):
        result.append(heapq.heappop(hlist))
        # result.append(-heapq.heappop(hlist)) # 내림차순

    return result

print(heapsort([34,65,23,4,6,5,2]))

# 정렬된 배열에서 특정한 원소 찾을 때 - biset 활용법 O(logN)
# left_value <= x <= right_value 인 원소의 개수를 쉽게 구할 수 있다.
from bisect import bisect_left, bisect_right
# 정렬된 순서를 유지하면서 리스트에 데이터를 삽입할 가장 왼쪽/오른쪽 인덱스를 찾는 함수.
def count_by_range(v_list, left_value, right_value):
    v_list.sort()
    right_index = bisect_right(v_list,right_value)
    left_index = bisect_left(v_list,left_value)
    return right_index - left_index

v_list = [5,6,2,7,6,8,2,4,8,9,3,56,76,983,523]
# 값이 4인 데이터 개수 출력
print(count_by_range(v_list, 6,6))
# 값이 [5,9] 범위에 있는 데이터 개수 출력
print(count_by_range(5,9))
print(v_list.sort())
