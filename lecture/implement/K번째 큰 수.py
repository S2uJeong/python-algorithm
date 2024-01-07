from itertools import combinations

def first_try(lang, k, num_list) :
    combis_list = list(combinations(num_list,3))

    sum_list = []
    for i in range(len(combis_list)) :
        sum_list.append(sum(combis_list[i]))

    # 중복제거
    remove_same = set(sum_list)
    sorted_list = sorted(remove_same,reverse=True)

    return sorted_list[k-1]

v_list = [18, 54, 46, 52, 28, 22, 23, 53, 28, 40]
print(first_try(10,3,v_list))

def example(lang, k, num_list):
    sum_list = []
    for i in range(lang):
        for j in range(i+1,lang):
            for m in range(j+1,lang):
                sum_list.append(num_list[i] + num_list[j] + num_list[m])

    remove_same = set(sum_list)
    sorted_list = sorted(remove_same, reverse=True)

    return sorted_list[k - 1]

print(example(10,3,v_list))