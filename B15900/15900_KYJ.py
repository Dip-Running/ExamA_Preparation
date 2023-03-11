from sys import stdin

N = int(stdin.readline())
adj = [[] for _ in range(N + 1)]
leaf = []
visited = [-1] + [0] * N

for n in range(N - 1):
    n1, n2 = map(int, stdin.readline().rstrip().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

stack =[[1, 0]]
while stack:
    node, cnt = stack.pop()
    visited[node] = 1

    if node != 1 and len(adj[node]) == 1:
        leaf.append(cnt)
        continue

    for n in adj[node]:
        if visited[n] == 0:
            stack.append([n, cnt + 1])

total = sum(leaf)
if total % 2:
    print('Yes')
else:
    print('No')