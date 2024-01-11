# sort() : O(nlogn) 대신 n번의 연산으로 하는 방법
def not_use_sort(target_list, input_list):
        p1 = p2 = 0
        result = []
        while p1 < len(target_list) and p2 < len(input_list):
            if target_list[p1] <= input_list[p2]:
                result.append(target_list[p1])
                p1 += 1
            else :
                result.append(input_list[p2])
                p2 += 1

        if p1 < len(target_list):
            result += target_list[p1:]
        if p2 < len(input_list):
            result += input_list[p2: ]

        return  result

# 몇 개의 케이스가 들어와도 정렬이 되도록 리팩토링! 재사용성을 높였음.
def sum_nlist_and_sort(n):
    result = []
    for _ in range(n):
        nums = list(map(int, input().split()))
        result = not_use_sort(result, nums)
    return result

def use_plus(n):
    result = []
    for _ in range(n):
        result += list(map(int,input().split()))
    result.sort()
    return result

def use_extend(n):
    result = []
    for _ in range(n):
        result.extend(list(map(int,input().split())))
    result.sort()
    return result

n = 2
#print(f'use_plus() : {use_plus(n)}')
#print(f'use_extend() : {use_extend(n)}')
print(sum_nlist_and_sort(4))
test_list = [1 ,10, 27, 39, 50, 61, 65, 70, 93, 93,
7, 51, 65, 66, 70, 82, 93,
14, 24, 35, 38, 45, 69, 78, 96, 97,
1, 15, 27, 29, 40, 50, 58, 63, 70, 74, 75, 82, 99 ]
test_list.sort()
print(test_list)