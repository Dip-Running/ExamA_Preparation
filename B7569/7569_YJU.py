from collections import deque
n,m,h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
visit = deque()
for i in range(h):
    for j in range(m):
        for idx, k in enumerate(matrix[i][j]):
            if k == 1:
                visit.append((i,j,idx))
dxdydz = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
while visit:
    x, y, z = visit.popleft()
    for dx, dy, dz in dxdydz:
        nx = x + dx
        ny = y + dy
        nz = z + dz
        if -1<nx<h and -1<ny<m and -1<nz<n and not matrix[nx][ny][nz]:
            matrix[nx][ny][nz] = matrix[x][y][z] + 1
            visit.append((nx,ny,nz))
answer = 0
check = 0
for i in range(h):
    for j in range(m):
        for k in matrix[i][j]:
            if not k:
                answer = 0
                check = 1
                break
            if answer < k:
                answer = k
        if check:
            break
    if check:
        break
if check:
    print(-1)
elif not check and not answer:
    print(answer)
else:
    print(answer -1)