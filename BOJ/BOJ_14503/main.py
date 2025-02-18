'''
    N x M 의 방
    각각의 칸은 벽 또는 빈 칸
    청소기는 상하좌우 방향성이 있다 (d)
        d = 0 (상) d = 1 (우) d = 2 (하) d = 3 (좌)
    방의 각 칸은 (r, c) 로 나타낼 수 있다
    좌상단이 (0, 0) 이다
    우하단은 (N-1, M-1) 이다

    동작
        1. 현재 칸이 처음 방문하는 칸이고, 빈 칸이라면 청소
        2. 현재 칸의 상하좌우에 청소가 안된 빈칸이 없는 경우
            1. 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진 후 1번 동작 시행
            2. 후진이 불가능하다면 종료
        3. 현재 칸의 상하좌우에 청소가 안된 빈칸이 있는 경우
            1. 반시계 방향으로 90도 회전
            2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
            3. 1번 동작 시행

    작동이 멈출 때까지 청소한 방의 개수 출력
'''

import sys

class Cleaner:
    def __init__(
            self, room_info, r, c, d, N, M
    ):
        self.room_info = room_info
        self.d_info = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.r, self.c, self.d = r, c, d
        self.N, self.M = N, M
        self.exit = False

    def check_now(self):
        if self.room_info[self.r][self.c] == '0':
            self.room_info[self.r][self.c] = '2'

    def check_around(self):
        for i in range(4):
            dr = self.r + self.d_info[i][0]
            dc = self.c + self.d_info[i][1]
            if 0 <= dr < self.N and 0 <= dc < self.M:
                if self.room_info[dr][dc] == '0':
                    return True

        return False

    def next_action(self, flag):
        if flag is True:
            for i in range(4):
                self.d = self.d = (self.d - 1) % 4

                dr = self.r + self.d_info[self.d][0]
                dc = self.c + self.d_info[self.d][1]

                if self.room_info[dr][dc] == '0':
                    self.r = dr
                    self.c = dc

                    return

        else:
            d = (self.d + 2) % 4

            dr = self.r + self.d_info[d][0]
            dc = self.c + self.d_info[d][1]

            if 0 <= dr < self.N and 0 <= dc < self.M:
                if self.room_info[dr][dc] != '1':
                    self.r = dr
                    self.c = dc

                    return

            self.exit = True
            return


N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room_info = [sys.stdin.readline().split() for _ in range(N)]

cleaner = Cleaner(room_info=room_info, r=r, c=c, d=d, N=N, M=M)

while not cleaner.exit:
    cleaner.check_now()
    flag = cleaner.check_around()
    cleaner.next_action(flag=flag)

count = 0
for n in range(N):
    for m in range(M):
        if cleaner.room_info[n][m] == '2':
            count += 1

print(count)