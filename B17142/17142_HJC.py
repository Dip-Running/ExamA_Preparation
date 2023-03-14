import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')
#####
import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 시작 할 수 있는 선택지
vir = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            vir.append([i, j])

# m개를 고르는 경우의 수
stpos = list(combinations(vir, m))

# 정답은 가능한 최댓값으로 선언
ans = sys.maxsize
# arr에 0이 있는지 체크용
zro_chk = False
# 조합이 dic 형태라 list 형태로 변환
for st in stpos:
    q = deque()
    for i, j in st:
        q.append([i, j])
    # 방문 체크용
    visited = [[0] * n for _ in range(n)]
    # 카운트용도
    cnt = [[0] * n for _ in range(n)]
    # 2를 어디에 바꿨는지 찾기 어려우므로 딥카피
    _arr = copy.deepcopy(arr)
    while q:
        x, y = deque.popleft(q)
        visited[x][y] = 1
        for dx, dy in dr:
            nx = x + dx
            ny = y + dy
            # 0이면 q에 append
            if 0 <= nx < n and 0 <= ny < n:
                if _arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt[nx][ny] = cnt[x][y] + 1
                    q.append([nx, ny])
                    _arr[nx][ny] = 2
                elif _arr[nx][ny] == 2 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    if [nx, ny] not in st:
                        cnt[nx][ny] = cnt[x][y] + 1
    # print(st)
    # for i in _arr:
    #     print(i)
    # print()
    # for j in cnt:
    #     print(j)
    # print()
    # print()
    # 시작 가능 점들은 카운트 취소
    for i, j in vir:
        cnt[i][j] = 0

    if 0 not in sum(_arr, []):
        zro_chk = True
        cnt_tmp = max(sum(cnt, []))
        ans = min(cnt_tmp, ans)
if not zro_chk:
    ans = -1
print(ans)
