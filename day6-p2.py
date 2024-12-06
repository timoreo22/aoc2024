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
    start_pos = None
    for l in f.readlines():
        line = list(l)
        try:
            idx = line.index('^')
            start_pos = pos = (len(area), idx)
            line[idx] = '.'
        except ValueError:
            pass
        area.append(line)
    print(pos)
    move = (-1, 0)
    visited = {pos}
    if do_visit(area, move, pos, visited):
        print("Error ! initial visit loops !")
        exit(1)
    # first iteration, all valid spots to drop items are
    spots = set([(x[0], x[1]) for x in visited.difference([start_pos])])
    looped = 0
    for s in spots:
        pos = start_pos
        move = (-1, 0)
        visited = {pos}
        area[s[0]][s[1]] = '#'
        if do_visit(area, move, pos, visited):
            looped += 1
        area[s[0]][s[1]] = '.'
    print(looped)
    f.close()


def do_visit(area, move, pos, visited) -> bool:
    while True:
        x = pos[0] + move[0]
        y = pos[1] + move[1]
        if x < 0 or x >= len(area) or y < 0 or y >= len(area[0]):
            return False
        if area[x][y] == '#':
            move = rotate(move)
        else:
            pos = (x, y, move)
            if pos in visited:
                return True
            visited.add(pos)


if __name__ == '__main__':
    main()