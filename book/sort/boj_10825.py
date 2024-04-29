array = []
for _ in range(int(input())) :
    name, lang, eng, math = input().split()
    array.append([name, int(lang), int(eng), int(math)])

array.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for arr in array:
    print(arr[0])