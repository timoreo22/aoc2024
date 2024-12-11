from math import floor
from functools import cache

@cache
def do_loop(num, count):
    if count == 0:
        return 1
    elif num == 0:
        return do_loop(1, count -1)
    else:
        digits = len("%i" % num)
        if round(digits % 2) == 0:
            mult = 10 ** (digits / 2)
            l = floor(num / mult)
            tot = int(num - (l * mult))
            return do_loop(l, count - 1) + do_loop(tot, count - 1)
        else:
            return do_loop(num * 2024, count - 1)

def main():
    f = open("day11-input.txt")
    rocks = [int(x) for x in f.read().strip().split()]
    total = 0
    for r in rocks:
        total += do_loop(r, 75)
    print(total)
    f.close()

if __name__ == '__main__':
    main()