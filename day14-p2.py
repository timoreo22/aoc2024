import re
from math import floor
from tqdm import trange
def main():
    f = open('day14-input.txt')
    output = open('day14-output.txt', 'w')
    robots: list[tuple[tuple[int,int],tuple[int,int]]] = []
    reg = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    max_x = 101 # 11
    max_y = 103 # 7
    for line in f.readlines():
        m = reg.match(line)
        robots.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))
    f.close()
    for ite in trange(60000):
        for i, robot in enumerate(robots):
            px = robot[0][0] + robot[1][0]
            py = robot[0][1] + robot[1][1]
            while px >= max_x:
                px -= max_x
            while py >= max_y:
                py -= max_y
            while px < 0:
                px += max_x
            while py < 0:
                py += max_y

            robots[i] = ((px, py), (robot[1][0], robot[1][1]))
        v_pos = {x[0] for x in robots}
        if ite % 101 == 67:
            print(ite + 1, file=output)
            for x in range(max_x):
                for y in range(max_y):
                    if (x,y) in v_pos:
                        print('#', end='', file=output)
                    else:
                        print('.', end='', file=output)
                print(file=output)
            print(file=output)
    output.close()
if __name__ == '__main__':
    main()