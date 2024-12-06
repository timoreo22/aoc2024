def rotate(move):
    if move == (-1,0):
        return 0, 1
    elif move == (0, 1):
        return 1, 0
    elif move == (1, 0):
        return 0, -1
    elif move == (0, -1):
        return -1, 0

def main():
    f = open('day6-input.txt', 'r')
    area = []
    pos = None
    for l in f.readlines():
        line = list(l)
        try:
            idx = line.index('^')
            pos = (len(area), idx)
            line[idx] = '.'
        except ValueError:
            pass
        area.append(line)
    print(pos)
    move = (-1, 0)
    visited = {pos}
    while True:
        x = pos[0] + move[0]
        y = pos[1] + move[1]
        if x < 0 or x >= len(area) or y < 0 or y >= len(area[0]):
            break
        if area[x][y] == '#':
            move = rotate(move)
        else:
            pos = (x, y)
            visited.add(pos)
    print(len(visited))
    f.close()

if __name__ == '__main__':
    main()