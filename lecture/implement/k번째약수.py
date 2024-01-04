def first_try(num,k) :
    numbers = []
    result = -1
    for i in range(1, num + 1):
        if num % i == 0:
            numbers.append(i)

    if len(numbers) < k:
        return result
    else:
        result = numbers[k - 1]
        return  result

print(first_try(6,3))

# for - else 문 활용
def example(num,k):
    cnt = 0
    result = 0
    for i in range(1,num+1) :
        if num % i == 0 :
            cnt +=1
        if cnt == k :
            result = i
            break
    else :
        result = -1

    return result

print(example(6,3))

# 240105 - 미완성
def second_try(num,k) :
    result_list = []
    result = 0
    divided_num = 0

    if num % 2 == 0 :
        divided_num = num // 2 -1
    else :
        divided_num = num // 2

    for i in range(1, divided_num+1) :
        if (num % i) == 0 :
            result_list.append(i)

    for j in result_list :
        if (num / j) == j :
            continue
        result_list.append(num//j)



