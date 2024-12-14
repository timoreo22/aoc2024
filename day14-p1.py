import re
from math import floor
def main():
    f = open('day14-input.txt')
    robots: list[tuple[tuple[int,int],tuple[int,int]]] = []
    reg = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    max_x = 101 # 11
    max_y = 103 # 7
    for line in f.readlines():
        m = reg.match(line)
        robots.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))
    f.close()
    for _ in range(100):
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
    # get robots in quadrants
    q_x = floor(max_x/2)
    q_y = floor(max_y/2)
    q_1 = 0
    q_2 = 0
    q_3 = 0
    q_4 = 0
    for r in robots:
        if r[0][0] > q_x:
            if r[0][1] > q_y:
                q_1 += 1
            elif r[0][1] < q_y:
                q_2 += 1
        elif r[0][0] < q_x:
            if r[0][1] > q_y:
                q_3 += 1
            elif r[0][1] < q_y:
                q_4 += 1
    print(q_4 , q_2 , q_1 , q_3)
    print(q_1 * q_2 * q_3 * q_4)

if __name__ == '__main__':
    main()