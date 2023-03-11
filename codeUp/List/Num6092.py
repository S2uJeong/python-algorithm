num = int(input());  # 부를 출석번호의 총 갯수
# 공백을 기준으로 문자열로 나뉘어져서 리스트가 만드어 진뒤, map 함수를 통해 int화 해준다.
callList = list(map(int, input().split()));  # 부른 출석번호의 나열

studentNum = [];
for i in range(1,24):
    studentNum.append(0);

for i in range(num):
    studentNum[callList[i]-1] += 1;

# List 압축해제 해서 간편하게 출력하는 방법 : *
print(*studentNum);

