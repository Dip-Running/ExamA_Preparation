import sys
sys.stdin = open('text.txt', 'r')
#####
from collections import deque

m, n, dim = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(dim)]
tom = deque()
for z in range(dim):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                tom.append([z, x, y])
dr = [[1, 0, 0], [-1, 0, 0],
      [0, -1, 0], [0, 1, 0],
      [0, 0, 1], [0, 0, -1]]
visited = [[[0]*m for _ in range(n)] for _ in range(dim)]
day = [[[0]*m for _ in range(n)] for _ in range(dim)]

while tom:
    z, x, y = tom.popleft()
    visited[z][x][y] = 1
    for dz, dx, dy in dr:
        nx = x + dx
        ny = y + dy
        nz = z + dz
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < dim and not visited[nz][nx][ny] and arr[nz][nx][ny] == 0:
            arr[nz][nx][ny] = 1
            visited[nz][nx][ny] = 1
            day[nz][nx][ny] = day[z][x][y] + 1
            tom.append([nz, nx, ny])
flag = False
for i in arr:
    for j in i:
        if 0 in j:
            flag = True

ans = -1
if not flag:
    for i in day:
        for j in i:
            ans = max(ans, max(j))
print(ans)