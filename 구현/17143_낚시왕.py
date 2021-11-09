import sys

def input():
    return sys.stdin.readline().rstrip()

# R = 격자판의 행의 수
# C = 격자판의 열의 수
# M = 상어의 총 마리수
R, C, M = map(int, input().split())

class Shark():
    def __init__(self, row, column, speed, direction, size):
        self.row = row
        self.column = column
        self.size = size
        self.direction = direction
        self.speed = speed
    # 상어의 움직임 방향과 속도를 기준으로 일단 움직여줌
    def moveSharks(self):
        if self.direction == 1:
            self.row = self.row - self.speed
        elif self.direction == 2:
            self.row = self.row + self.speed
        elif self.direction == 3:
            self.column = self.column + self.speed
        elif self.direction == 4:
            self.column = self.column - self.speed
    def adjustSharkLocationPointer(self):
        while self.row > R or self.row < 1:
            if self.direction == 1 and self.row < 1:
                self.row = -self.row + 2
                self.direction = 2
            if self.direction == 2 and self.row > R:
                self.row = R - abs(self.row - R)
                self.direction = 1
        while self.column > C or self.column < 1:
            if self.direction == 3 and self.column > C:
                self.column = C - abs(self.column - C)
                self.direction = 4
            if self.direction == 4 and self.column < 1:
                self.column = -self.column + 2
                self.direction = 3

Sharks = []
for _ in range(M):
    row, column, speed, direction, size = map(int, input().split())
    tmp = Shark(row, column, speed, direction, size)
    Sharks.append(tmp)
score = 0

for second in range(1,C+1):
    removing_Sharks=[]
    Sharks.sort(key= lambda x : x.row)
    for shark in Sharks:
        if shark.column == second:
            score += shark.size
            Sharks.remove(shark)
            break
    for shark in Sharks:
        shark.moveSharks()
        shark.adjustSharkLocationPointer()
        
    for shark in Sharks:
        for otherSharks in Sharks:
            if shark == None or otherSharks == None:
                continue
            if shark.row == otherSharks.row and shark.column == otherSharks.column and shark.size != otherSharks.size:
                if shark.size > otherSharks.size:
                    removing_Sharks.append(otherSharks)
                else:
                    removing_Sharks.append(shark)
    for removes in removing_Sharks:
        if removes in Sharks:
            Sharks.remove(removes)
print(score)