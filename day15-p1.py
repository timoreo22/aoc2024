def check_move(robot: tuple[int,int], dire: tuple[int,int], wall_set, box_set) -> bool:
    px = robot[0] + dire[0]
    py = robot[1] + dire[1]
    if (px,py) in wall_set:
        return False
    if (px, py) in box_set:
        if check_move((px,py), dire, wall_set, box_set):
            box_set.remove((px,py))
            box_set.add((px + dire[0],py + dire[1]))
            return True
        else:
            return False
    return True


def main():
    f = open('day15-input.txt')
    wall_set = set()
    box_set = set()
    robot = (0,0)
    y = 0
    while True:
        line = f.readline()
        if line == '\n':
            break
        for x, c in enumerate(line.strip()):
            if c == '#':
                wall_set.add((x,y))
            elif c == 'O':
                box_set.add((x,y))
            elif c == '@':
                robot = (x,y)
        y += 1
    moves = f.read()
    f.close()
    for m in moves:
        if m == '\n':
            continue
        dire = None
        if m == '^':
            dire = (0, -1)
        elif m == 'v':
            dire = (0, 1)
        elif m == '<':
            dire = (-1, 0)
        elif m == '>':
            dire = (1, 0)
        if dire is not None:
            if check_move(robot, dire, wall_set, box_set):
                robot = (robot[0] + dire[0], robot[1] + dire[1])
    total = 0
    for b in box_set:
        total += b[0] + b[1] * 100
    print(total)
if __name__ == '__main__':
    main()