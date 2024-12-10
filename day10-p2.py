def main():
    f = open('day10-input.txt')
    top: list[list[int]] = [[int(y) for y in x.strip()] for x in f.readlines()]
    f.close()
    total = 0
    for x,ar in enumerate(top):
        for y,el in enumerate(ar):
            if el == 0:
                total += do_lookup(x,y, top, 1)
    print(total)


def do_lookup(x: int, y: int, top: list[list[int]], num: int) -> int:
    if num > 9:
        return 1
    pos = [(1,0),(0,1),(-1,0),(0,-1)]
    total = 0
    for p in pos:
        px = x + p[0]
        py = y + p[1]
        if px < 0 or px >= len(top) or py < 0 or py >= len(top[0]):
            continue
        if top[px][py] == num:
            total += do_lookup(px, py, top, num + 1)
    return total

if __name__ == '__main__':
    main()