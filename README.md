# 📁 파이썬 알고리즘 문제풀이 REPO 
- 파이썬 공식문서 : https://docs.python.org/ko/3/library/index.html
---
## To-do
### 복습
- [구현] 
  - pgm_60059.py (자물쇠와 열쇠)
  - pgm_60061.py (기둥과 보 설치)
- [그리디] 
  - book.314_만들 수 없는 금액
  - book.315_볼링공 고르기
- [dfs/bfs] 
  - 백준 인구이동 : https://www.acmicpc.net/problem/16234
  - 연구소 복습 : https://www.acmicpc.net/problem/14502
  - dfs/네트워크 : https://school.programmers.co.kr/learn/courses/30/lessons/43162
- [정렬]
  - book/sort/pgm_42889.py : 실패율
- 문제집
  - https://covenant.tistory.com/224
  - https://github.com/tony9402/baekjoon/tree/main

## 규칙
- 새로 알게된 부분은 commit 메세지로 간략히 표현

## 제한사항
### 시간 계산 코드
```python
import time
start_time = time.time()
end_time = time.time()

print("time :", end_time - start_time)
```
### ⏰ 입력갯수에 따른 알고리즘 시간복잡도 계산방법

입력의 크기를 시간 복잡도에 대입해서 얻은 반복문 수행 횟수에 대해, 1초 당 반복문 수행 횟수가 1억($10^8$)을 넘어가면 시간 제한을 초과할 가능성이 있다.


시간제한이 1초인 문제를 만났을 때, 일반적인 기준

입력이 10,000,000 개의 경우: O(N) 알고리즘

입력이 50,000 개인 경우: O(N * log N) 알고리즘

입력이 10,000 개인 경우: O(N * N) 알고리즘

입력이 400개: O(N * N * N) 알고리즘


입력이 100개 이하라면 대체로 어떤 알고리즘을 써도 풀릴 가능성이 높고, 입력이 매우 작은 경우는 완전탐색으로도 문제를 풀 수 있을 가능성이 높다.

---
## 📄 메모

### 01_자료구조별
- queue
  - `while queue : ` 구문을 조건문으로 많이 사용한다. 
  - 순서는 바뀌면 안되다던지 순서대로 를 강조하는 문제에서 주로 사용하는 것 같다. 

### 02_기능별

- if 조건문
  - and 명령어로 여러 조건 수식을 적으면, 먼저 나오는 수식부터 검증하고 FALSE인게 나오면 그 다음 수식은 검증하지 않는다.

### 03_좋은 수식 및 로직
- list 탐색시, 왼쪽 -> 오른쪽 방향 유지하면서 len 안 넘게 탐색 반복하는 방법 
- 관련 파일 : programmers/자료구조/프로세스.py
  ```python
  cur = 0
  arr = list(range(1,100))
  while True :
      tmp = arr[cur%len(arr)]
      if tmp == 50:
          break
      cur += 1
  ```
### 04_알고리즘별
- bfs, dfs
  - bfs는 **(최단)거리**를 구할 때 주로 사용 
  - dfs는 **경우의 수**를 구할 때 주로 사용 
