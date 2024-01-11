def first_try(p_list) :
    for _ in range(10):
        idx_str, idx_end = map(int, input().split())
        for i in range(idx_str, idx_str + (idx_end - idx_str + 1) // 2):
            p_list[i], p_list[idx_end] = p_list[idx_end], p_list[i]
            idx_end = idx_end - 1
    return list(p_list[1:21])

def example(p_list):
    for _ in range(10):
        idx_str, idx_end = map(int, input().split())
        for i in range((idx_end - idx_str) // 2):
            # 🟡 인덱스 활용 보단 몇번 반복할건지로만 range를 짜서 간단해짐
            p_list[idx_end-i], p_list[idx_end-i] = p_list[idx_end-i], p_list[idx_end-i]
    return list(p_list[1:21])

nums = list(range(21))  # 문제에서 주어지는 인덱스와 일치 시키기 위해 0 ~ 20 으로 생성
print(f'first_try() : {first_try(nums)}')
print(f'example() : {example(nums)}')


