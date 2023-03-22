list_range, swap_count = map(int,input().split())

list_A = list(map(int,input().split()))
list_B = list(map(int,input().split()))

list_A.sort()
list_B.sort(reverse=True)

for i in range(swap_count):
    if list_A[i] < list_B[i]:
        list_A[i], list_B[i] = list_B[i], list_A[i]
    else:
        break

print(sum(list_A))