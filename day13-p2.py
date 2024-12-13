import re
from sympy import solve
from sympy.abc import x,y

def main():
    f = open("day13-input.txt")
    file = f.read()
    f.close()
    b_re = re.compile(r'Button [AB]: X\+(\d+), Y\+(\d+)')
    prize_re = re.compile(r'Prize: X=(\d+), Y=(\d+)')
    total = 0
    for game in file.split('\n\n'):
        data = game.split('\n')
        m = b_re.match(data[0])
        a_x = int(m.group(1))
        a_y = int(m.group(2))
        m = b_re.match(data[1])
        b_x = int(m.group(1))
        b_y = int(m.group(2))
        m = prize_re.match(data[2])
        target_x = int(m.group(1)) + 10000000000000
        target_y = int(m.group(2)) + 10000000000000
        # find x
        sols = solve([x*b_x + y*a_x - target_x, x*b_y + y*a_y - target_y], x,y, dict=True)
        if len(sols) > 1:
            print("Warn multi sols", sols)
        if len(sols) > 0:
            s = sols[0]
            if s[x].is_integer and s[y].is_integer:
                total += sols[0][x] * 1 + sols[0][y] * 3
    print(total)





if __name__ == '__main__':
    main()