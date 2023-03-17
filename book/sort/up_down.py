count_num = int(input())

num_list = []

for i in range(count_num):
    num = int(input())
    num_list.append(num)

num_list.sort(reverse=True)

print(*num_list)