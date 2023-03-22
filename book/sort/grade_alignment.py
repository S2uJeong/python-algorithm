student_num = int(input())

list = []
for i in range(student_num):
    input_data = input().split()
    list.append((input_data[0], int(input_data[1])))  # 리스트.append( (값,값) ) 를 통해 리스트 안에 튜플을 담을 수 있다.

list.sort(key=lambda x : x[1])

for student in list:
    print(student[0], end=' ')


