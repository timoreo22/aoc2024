from collections import defaultdict


def main():
    f = open('day8-input.txt', 'r')
    antennas = defaultdict(lambda : [])
    max_x = 0
    max_y = 0
    for x, line in enumerate(f.readlines()):
        for y, c in enumerate(line):
            if c != '.' and c != '\n':
                antennas[c].append((x,y))
            if y > max_y:
                max_y = y
        if x > max_x:
            max_x = x
    max_y -= 1
    antinodes = set()
    for val in antennas.values():
        for el in val:
            for other in val:
                if el != other:
                    diffx = el[0]
                    diffy = el[1]
                    while not (diffx < 0 or diffx > max_x or diffy < 0 or diffy > max_y):
                        antinodes.add((diffx, diffy))
                        diffx += (el[0] - other[0])
                        diffy += (el[1] - other[1])
    print(len(antinodes))
    f.close()

if __name__ == '__main__':
    main()