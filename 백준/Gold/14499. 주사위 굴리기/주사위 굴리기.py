from enum import Enum
import sys
input = lambda: sys.stdin.readline().rstrip()
output = sys.stdout.write
class Dir(Enum):
    EAST = 1
    WEST = 2
    NORTH = 3
    SOUTH = 4
    UP = 5
    DOWN = 6
dice: dict[Dir, int] = {
    Dir.EAST: 3,
    Dir.WEST: 4,
    Dir.NORTH: 2,
    Dir.SOUTH: 5,
    Dir.UP: 6,
    Dir.DOWN: 1}
diff: dict[Dir, tuple[int, int]] = {
    Dir.EAST: (0, 1),
    Dir.WEST: (0, -1),
    Dir.NORTH: (-1, 0),
    Dir.SOUTH: (1, 0)
}
val = [0] * 7
def face(dice: dict[Dir, int], dir: Dir):
    return val[dice[dir]]
def setface(dice: dict[Dir, int], dir: Dir, setvalue: int):
    val[dice[dir]] = setvalue
def roll(dice: dict[Dir, int], dir: Dir):
    if dir == Dir.EAST:
        return {
            Dir.EAST: dice[Dir.UP],
            Dir.WEST: dice[Dir.DOWN],
            Dir.NORTH: dice[Dir.NORTH],
            Dir.SOUTH: dice[Dir.SOUTH],
            Dir.UP: dice[Dir.WEST],
            Dir.DOWN: dice[Dir.EAST]
        }
    elif dir == Dir.WEST:
        return {
            Dir.EAST: dice[Dir.DOWN],
            Dir.WEST: dice[Dir.UP],
            Dir.NORTH: dice[Dir.NORTH],
            Dir.SOUTH: dice[Dir.SOUTH],
            Dir.UP: dice[Dir.EAST],
            Dir.DOWN: dice[Dir.WEST]
        }
    elif dir == Dir.NORTH:
        return {
            Dir.EAST: dice[Dir.EAST],
            Dir.WEST: dice[Dir.WEST],
            Dir.NORTH: dice[Dir.UP],
            Dir.SOUTH: dice[Dir.DOWN],
            Dir.UP: dice[Dir.SOUTH],
            Dir.DOWN: dice[Dir.NORTH]
        }
    elif dir == Dir.SOUTH:
        return {
            Dir.EAST: dice[Dir.EAST],
            Dir.WEST: dice[Dir.WEST],
            Dir.NORTH: dice[Dir.DOWN],
            Dir.SOUTH: dice[Dir.UP],
            Dir.UP: dice[Dir.NORTH],
            Dir.DOWN: dice[Dir.SOUTH]
        }
n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(lambda x: Dir(int(x)), input().split()))
result = []
for dir in cmds:
    dx, dy = diff[dir]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    dice = roll(dice, dir)
    if grid[x][y] == 0:
        grid[x][y] = face(dice, Dir.DOWN)
    else:
        setface(dice, Dir.DOWN, grid[x][y])
        grid[x][y] = 0
    result.append(face(dice, Dir.UP))
output("\n".join(map(str, result)))