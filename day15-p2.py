def check_move(robot: tuple[int | float,int], dire: tuple[int | float,int], wall_set, box_set: list[tuple[int | float,int]], good_edge: set[tuple[int | float, int]],box_mode: bool) -> bool:
    px = robot[0] + dire[0]
    py = robot[1] + dire[1]
    if (px,py) in wall_set:
        return False
    if (px, py) in box_set:

        if dire[0] != 0:
            if check_move((px, py), dire, wall_set, box_set, good_edge, False):
                box_set.remove((px, py))
                if (px,py) in good_edge:
                    good_edge.remove((px,py))
                    good_edge.add((px + dire[0],py + dire[1]))

                box_set.append((px + dire[0], py + dire[1]))
                return True
            else:
                return False
        else:
            if (px,py) in good_edge:
                d = 0.5
            else:
                d = -0.5
            if check_move((px,py), dire, wall_set, box_set, good_edge,True) and check_move((px + d, py), dire, wall_set, box_set,good_edge, True):
                if not box_mode:
                    check_move((px, py), dire, wall_set, box_set, good_edge,False)
                    check_move((px + d, py), dire, wall_set, box_set, good_edge,False)
                    box_set.remove((px,py))
                    box_set.remove((px + d, py))
                    if (px, py) in good_edge:
                        good_edge.remove((px, py))
                        good_edge.add((px + dire[0], py + dire[1]))
                    elif (px + d, py) in good_edge:
                        good_edge.remove((px + d, py))
                        good_edge.add((px + d + dire[0], py + dire[1]))
                    box_set.append((px + dire[0],py + dire[1]))
                    box_set.append((px + d + dire[0], py + dire[1]))
                return True
            else:
                return False
    return True


def print_area(robot, wall_set, box_set, max_y, max_x):
    for y in range(max_y):
        for ax in range(0,(max_x+1)*2):
            x = ax/2
            if robot == (x,y):
                print('@', end='')
            elif (x,y) in wall_set:
                print('#', end='')
            elif (x,y) in box_set:
                print('[', end='')
            else:
                print('.',end='')
        print()


def main():
    f = open('day15-input.txt')
    wall_set = set()
    good_edge = set()
    box_set = []
    robot = (0,0)
    y = 0
    max_x = 0

    while True:
        line = f.readline()
        if line == '\n':
            break
        for x, c in enumerate(line.strip()):
            if c == '#':
                wall_set.add((x,y))
                wall_set.add((x + 0.5, y))
            elif c == 'O':
                good_edge.add((x,y))
                box_set.append((x,y))
                box_set.append((x + 0.5,y))
            elif c == '@':
                robot = (x,y)
        max_x = x
        y += 1
    moves = f.read()
    f.close()
    for m in moves:
        if m == '\n':
            continue
        # print_area(robot, wall_set, box_set, y, max_x)
        dire = None
        if m == '^':
            dire = (0, -1)
        elif m == 'v':
            dire = (0, 1)
        elif m == '<':
            dire = (-0.5, 0)
        elif m == '>':
            dire = (0.5, 0)
        if dire is not None:
            if check_move(robot, dire, wall_set, box_set, good_edge, False):
                robot = (robot[0] + dire[0], robot[1] + dire[1])
    total = 0
    print_area(robot, wall_set, box_set, y, max_x)
    for b in good_edge:
        print(b)
        total += b[0]*2 + b[1] * 100
    print(total)
if __name__ == '__main__':
    main()