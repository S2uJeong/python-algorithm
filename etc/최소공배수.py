num1, num2 = map(int, input().split())

for i in range(max(num1,num2), num1*num2 +1 ) :
    if i % num1 == 0 and i % num2 == 0 :
        print(i)
        break