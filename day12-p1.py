def search_area(x: int, y: int, visited: set[tuple[int,int]], target: str, areas: list[list[str]]) -> tuple[int, int]:
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    perimeter = 0
    area = 1
    for d in directions:
        px = x + d[0]
        py = y + d[1]
        if px < 0 or px >= len(areas) or py < 0 or py >= len(areas[0]) or areas[px][py] != target:
            perimeter += 1
            continue

        if (px, py) not in visited:
            visited.add((px, py))
            n_area, n_perim = search_area(px, py, visited, target, areas)
            area += n_area
            perimeter += n_perim
    return area, perimeter



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
                area, perim = search_area(x, y, new_seen, areas[x][y], areas)
                total += area * perim
                visited.update(new_seen)
    print(total)

if __name__ == '__main__':
    main()