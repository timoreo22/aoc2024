from collections import defaultdict


def search_area(x: int, y: int, visited: set[tuple[int,int]], target: str, areas: list[list[str]], dir_side: defaultdict[tuple[int,int],set[tuple[int, int]]]) -> tuple[int, int]:
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    sides = 0
    area = 1
    n_count = set()
    for d in directions:
        px = x + d[0]
        py = y + d[1]
        if px < 0 or px >= len(areas) or py < 0 or py >= len(areas[0]) or areas[px][py] != target:
            n_count.add(d)
            if d not in dir_side[(x,y)]:
                sides += 1
    for d in directions:
        px = x + d[0]
        py = y + d[1]
        if d[0] == 0:
            n_temp = n_count.difference({(0, -1)}).difference({(0, 1)})
        else:
            n_temp = n_count.difference({(-1, 0)}).difference({(1, 0)})
        while not (px < 0 or px >= len(areas) or py < 0 or py >= len(areas[0]) or areas[px][py] != target):
            to_rem = set()
            for extra in n_temp:
                pdx = px + extra[0]
                pdy = py + extra[1]
                if not (pdx < 0 or pdx >= len(areas) or pdy < 0 or pdy >= len(areas[0]) or areas[pdx][pdy] != target):
                    to_rem.add(extra)
            n_temp.difference_update(to_rem)
            dir_side[(px, py)].update(n_temp)
            px += d[0]
            py += d[1]
    # print(x,y,sides)
    for d in directions:
        px = x + d[0]
        py = y + d[1]

        if px < 0 or px >= len(areas) or py < 0 or py >= len(areas[0]) or areas[px][py] != target:
            continue

        if (px, py) not in visited:
            visited.add((px, py))

            n_area, n_perim = search_area(px, py, visited, target, areas, dir_side)
            area += n_area
            sides += n_perim
    return area, sides



def main():
    f = open('day12-input.txt', 'r')
    areas = [[y for y in x.strip()] for x in f.readlines()]
    f.close()
    visited = set()
    total = 0
    for x in range(len(areas)):
        for y in range(len(areas[x])):
            if (x,y) not in visited:
                new_seen = set()
                new_seen.add((x,y))
                area, sides = search_area(x, y, new_seen, areas[x][y], areas, defaultdict(lambda : set()))
                # print(area, sides)
                total += area * sides
                visited.update(new_seen)
    print(total)

if __name__ == '__main__':
    main()