def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else :
        return binary_search(array, target, start+1, end)

target = 2
array = [1,2,3,4,5,6,7,8,9]
result = binary_search(array, target, 0, len(array)-1)
if result == None:
    print("원소가 존재 하지 않습니다.")
else:
    print(result + 1) # 몇 번째에 있는지 출력 하려면 index는 0부터이므로 1 더해줌