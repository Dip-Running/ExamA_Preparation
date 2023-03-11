from sys import stdin

'''
노드 정보는 정렬되지 않은 상태로 입력됨
인접 노드 정리 후, 리프노드만 찾아내면 됨
리프노드 -> 인접 노드가 1개인 노드
루트노드부터 시작해 스택에 노드 정보와 거리를 추가해가며
리프노드를 발견했을 때 거리를 리프 리스트에 저장
'''
N = int(stdin.readline())
adj = [[] for _ in range(N + 1)] # 인접 노드 저장
leaf = [] # root - leaf 거리 저장할 리스트
visited = [-1] + [0] * N # 방문표시 -> 정렬 불가, idxerror 방지

for n in range(N - 1):
    n1, n2 = map(int, stdin.readline().rstrip().split())
    adj[n1].append(n2) # 인접 노드 추가
    adj[n2].append(n1)

stack =[[1, 0]] # 루트 노드, 루트 거리
while stack:
    node, cnt = stack.pop() # 노드, 거리
    visited[node] = 1 # 방문 표시

    if node != 1 and len(adj[node]) == 1: # 루트가 아니고, 인접 노드가 1개이면 -> 리프 노드
        leaf.append(cnt) # 거리 추가
        continue

    for n in adj[node]: # 인접 노드 조사
        if visited[n] == 0: # 방문하지 않았다면
            stack.append([n, cnt + 1]) # 스택에 추가

'''
선 : 성원, 후 : 형석
선이 이겨야 하므로, 모든 게임말이 움직이는 총 거리를 2로(인원 수)로 나눌 시
나머지가 1이면 마지막에 한 번 더 가게 되는 것은 선 -> 선이 이김
나머지가 0이면 후가 마지막으로 가게 되고, 선은 말이 없어서 지게 됨
'''
total = sum(leaf)

if total % 2:
    print('Yes')
else:
    print('No')