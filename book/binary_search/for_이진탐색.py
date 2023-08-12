def binary_search(array, target, start, end):

    while start <= end:
        # 🔴 오답노트 : mid를 while 바깥에 표기함. 손으로 순차적으로 그려보며 파악함
        mid = (start + end) // 2
        if array[mid] == target :
            return mid
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return None

result = binary_search([1,2,3,4,5,6,7,8,9,10],4,0,9)

if result == None :
    print("None")
else :
    print(result + 1)