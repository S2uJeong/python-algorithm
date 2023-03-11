# 6045번 문제
a,b,c = input().split();

sum = int(a) + int(b) + int(c)
average = round( float(sum/3) , 2);

print(sum,'{:.2f}'.format(average)); # 표현식을 {}에 넣고 '' 도 넣어야 함에 유의

