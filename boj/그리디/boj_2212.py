"""
센서 위치 : 0 ~ 1_000_000
센서의 개수 : 1 ~ 10_000 (N)
집중국 개수 : 1 ~ 1_000 (K)
모든 센서가 하나의 집중국에는 들어야 하며, 수신 영역의 '합'을 최소화하는 K개의 집중국 나열 하기

- 센서의 거리 차이 중 제일 차이가 많이 나는 위치에 집중국을 세워 수신 영역을 줄인다.
"""
N = int(input().rstrip())
K = int(input().rstrip())
sensors = list(map(int,input().split()))
sensors.sort() # 센서의 차이를 구하기 위해 정렬한다.

if N <= K: # 집중국이 넉넉하면 수신영역은 0이다.
    print(0)
else:
    diff = []
    for i in range(1,len(sensors)):
        diff.append(sensors[i] - sensors[i-1])
    diff.sort(reverse=True) # 센서 거리가 먼 것부터 집중국으로 커버하기 위해 정렬

    print(sum(diff[K-1:])) # 제일 큰 차이를 집중국과 다른 집중국과의 거리라고 생각하고 diff[K-1]부터 더해줌
