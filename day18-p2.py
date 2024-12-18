from collections import defaultdict
from math import sqrt
import heapq

from tqdm import tqdm


def get_heurisitc(x, y, end):
    return sqrt((x - end[0]) ** 2 + (y - end[1]) ** 2)

def main():
    f = open('day18-input.txt')
    invalid = set()
    total_count = 1024 # 1024
    to_invalidate = []
    for l in f.readlines():
        coords = l.split(',')
        if len(coords) >= 2:
            if total_count <= 0:
                to_invalidate.append((int(coords[0]), int(coords[1])))
            else:
                total_count -= 1
                invalid.add((int(coords[0]), int(coords[1])))
    f.close()
    row = 71 #71
    col = 71 #71
    last_added = None
    with tqdm(total=len(to_invalidate)) as bar:
        while has_path(col, invalid, row):
            last_added = to_invalidate.pop(0)
            invalid.add(last_added)
            bar.update()
    print(last_added)


def has_path(col, invalid, row):
    start = (0, 0)
    end = (row - 1, col - 1)
    dist = defaultdict(lambda: 1e9)
    x = start[0]
    y = start[1]
    dist[(x, y)] = 0
    to_visit = []
    heapq.heappush(to_visit, (0, x, y))
    while len(to_visit) > 0:
        _, x, y = heapq.heappop(to_visit)
        if (x, y) == end:
            return True
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in dire:
            px = x + d[0]
            py = y + d[1]
            if 0 <= px < col and 0 <= py < row and (px, py) not in invalid:
                if dist[(x, y)] + 1 < dist[(px, py)]:
                    dist[(px, py)] = dist[(x, y)] + 1
                    heuristic = get_heurisitc(px, py, end)
                    for i, el in enumerate(to_visit):
                        if el[1] == px and el[2] == py:
                            to_visit[i][0] = dist[(px, py)] + heuristic
                            to_visit.sort(key=lambda x: x[0])
                    else:
                        heapq.heappush(to_visit, (dist[(px, py)] + heuristic, px, py))
    return False


if __name__ == '__main__':
    main()