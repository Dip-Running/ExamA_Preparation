import sys
from collections import deque
from itertools import combinations
'''
[1] M개의 바이러스 부분집합
[2] 델타탐색 -> 걸리는 시간 리스트 추가
[3] 최솟값 찾기

입력 데이터) 0 : 빈공간, 1 : 벽, 2 : 바이러스 위치(비활성화, 활성화)
바이러스) 활성화 : 시작 위치, 비활성화 : 활성화된 바이러스를 만날 시 빈공간 취급 but 최대 턴수로 저장되진 X
출력) 기본적으로 전부 바이러스화하는데 걸리는 시간, 만약 불가능하다면 -1
'''

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
N, M = map(int, input().split())
v = [] # 바이러스가 들어있는 위치를 담을 리스트
data = [] # 입력 데이터 받는 리스트
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상, 우, 하, 좌
ans = [] # 걸리는 시간 담는 리스트
emptycnt = 0 # 비어있는 공간 수

for n in range(N): # 입력받기 -> 시간 최소화
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    for m in range(N):
        if l[m] == 2: # 바이러스가 들어있는 위치일 때
            v.append([n, m]) # 바이러스 리스트에 추가
        elif l[m] == 0: # 빈공간일 때
            emptycnt += 1 # 추가
    data.append(l)

if emptycnt == 0: # 빈공간이 없을 때
    print(0) # 전부 바이러스이므로 시간이 걸리지 X

else: # 빈공간이 있을 때
    '''
    [1] M개의 바이러스 부분집합 구하기
    '''
    subset = list(combinations(v, M))  # v 리스트에서 M개의 원소를 가진 부분집합들

    for sub in subset: # 부분집합 하나씩 탐색
        visited = [[-1] * N for _ in range(N)] # 방문하는데 걸리는 시간 저장, 기본으로 -1(시작점이 0이어서)
        q = deque()

        for i, j in sub: # 시작점
            visited[i][j] = 0 # M개의 시작점 0으로 변경
            q.append([i, j]) # 큐에 추가

        mx = 0 # 끝까지 도달했을 때 시간
        while q:
            i, j = q.popleft()
            '''
            [2] 델타탐색 -> 걸리는 시간 리스트 추가
            '''
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N: # 범위 내
                    if data[ni][nj] == 0 and visited[ni][nj] == -1: # 비어있는 공간, 방문하지 X
                        q.append([ni, nj])
                        visited[ni][nj] = visited[i][j] + 1
                        mx = visited[ni][nj] # 최대값 갱신 -> 결국 마지막 턴이 최대값
                    elif data[ni][nj] == 2 and visited[ni][nj] == -1: # 바이러스 위치, 방문하지 X
                        q.append([ni, nj])
                        visited[ni][nj] = visited[i][j] + 1


        for i in range(N): # 전체 탐색 data, visited
            if mx == 10000: # 아래 반복문에서 break가 발생했을 때 반복문 탈출
                break
            for j in range(N):
                if data[i][j] == 0 and visited[i][j] == -1: # 빈공간에 방문하지 않았을 때
                    mx = 10000 # 최대값 불가능한 수로 변경
                    break

        ans.append(mx) # 걸리는 시간 추가

    '''
    [3] 최솟값 찾기
    '''
    mn = min(ans)
    if mn == 10000: # 모든 부분집합에서 도달하지 못했을 때
        print(-1)
    else:
        print(mn)