num, x = map(int, input().split())
nums = [int(i) for i in str(num)]

res = []
for num in nums:
    while res and x > 0 and res[-1] < num:
        res.pop()
        x -= 1
    res.append(num)

if x != 0:
    for _ in range(x):
        res.pop()

for i in res:
    print(i,end='')

