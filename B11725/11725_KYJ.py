import sys
from collections import deque
sys.stdin = open('input.txt')

'''
[1] 인접 노드 2차원 리스트 정리
[2] 1을 루트로 bfs
'''

N = int(input())
nodes = [[] for _ in range(N + 1)] # 인접 노드 정보 저장
parents = [0] * (N + 1) # idx : 자식, val : 부모
visited = [0] * (N + 1) # 방문 표시

for n in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split()) # 데이터 입력
    nodes[n1].append(n2) # 인접 노드 추가
    nodes[n2].append(n1)

q = deque() # dfs
for r in nodes[1]: # root에 연결된 노드
    q.append(r) # 큐에 추가
    parents[r] = 1 # 해당 노드들은 부모가 루트
visited[1] = 1 # 루트 노드 방문 표시

while q:
    parent = q.popleft()
    visited[parent] = 1
    for c in nodes[parent]:
        if visited[c] != 1: # 방문하지 않았다면
            parents[c] = parent # 자식노드 인덱스에 부모값 추가
            q.append(c) # 자식 큐에 추가

for n in range(2, N + 1):
    print(parents[n])