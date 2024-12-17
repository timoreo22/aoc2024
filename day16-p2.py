import copy
from collections import defaultdict
from typing import TypeAlias
from tqdm import trange
VertexDir: TypeAlias = tuple[int,int,tuple[int,int]]

def build_graph(valid, graph: defaultdict[VertexDir,dict[VertexDir,int]]):
    dire = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for current_dir in dire:
        for v in valid:
            c_dir = [current_dir, (current_dir[1], current_dir[0]), (-current_dir[1], -current_dir[0])]
            for d in c_dir:
                cost = 1001
                if d == current_dir:
                    cost = 1
                px = v[0] + d[0]
                py = v[1] + d[1]
                if (px,py) in valid:
                    if (px,py) not in graph[(v[0], v[1], current_dir)]:
                        graph[(v[0], v[1], current_dir)][(px,py, d)] = cost

def timstra(start: VertexDir, graph: defaultdict[VertexDir,dict[VertexDir,int]]):
    distances: dict[VertexDir, int | float] = {}
    prev: dict[VertexDir, VertexDir | None] = {}
    to_visit: list[VertexDir] = []
    for v in graph.keys():
            distances[v] = 1e9
            prev[v] = None
            to_visit.append(v)
    distances[start] = 0
    for _ in trange(len(to_visit)):
        u = min(to_visit, key=distances.__getitem__)
        to_visit.remove(u)
        for v in graph[u].keys():
            if v not in to_visit:
                continue
            alt = distances[u] + graph[u][v]
            if alt < distances[v]:
                distances[v] = alt
                prev[v] = u
    return distances, prev

def get_shortest_path(graph: defaultdict[VertexDir,dict[VertexDir,int]], start: VertexDir, end: tuple[int,int]) -> tuple[list[VertexDir], int]:
    dist, prev = timstra(start, graph)

    dire = [(-1,0),(0,1),(1,0),(0,-1)]
    m_d = ()
    m = 1e10
    for d in dire:
        if dist[(end[0],end[1], d)] < m:
            m = dist[(end[0],end[1], d)]
            m_d = d
    s: list[VertexDir] = []
    u: VertexDir = (end[0], end[1], m_d)

    if prev[u] is not None or u == (start[0], start[1], (1, 0)):
        while u is not None:
            s.insert(0, u)
            u = prev[u]
    return s, m


def main():
    f = open('day16-input.txt')
    start = ()
    end = ()
    valid = set()
    for y, l in enumerate(f.readlines()):
        for x,c in enumerate(l):
            if c == '.':
                valid.add((x,y))
            elif c == 'E':
                end = (x,y)
                valid.add((x,y))
            elif c == 'S':
                start = (x,y)
                valid.add((x,y))
    # build graph
    graph: defaultdict[VertexDir, dict[VertexDir, int]] = defaultdict(lambda : {})
    # initial
    dire = [(-1,0),(0,1),(1,0),(0,-1)]
    build_graph(valid, graph)
    print(start)
    print(graph[(1, start[1], (1,0))])
    print("Points:",len(valid))
    short_path, short_cost = get_shortest_path(graph, (start[0], start[1], (1,0)), end)
    a = [short_path]
    costs = {tuple(short_path): short_cost}
    print(a)
    b = []
    # https://en.wikipedia.org/wiki/Yen%27s_algorithm
    for k in trange(1,11):
        for i in trange(len(a[k - 1]) - 2):
            spur = a[k-1][i]
            rootPath = a[k-1][:i]
            c_graph = copy.deepcopy(graph)
            for p in a:
                if rootPath == p[:i]:
                    try:
                        c_graph[p[i]].pop(p[i + 1])
                    except KeyError:
                        pass
            for rootPathNode in rootPath:
                if rootPathNode != spur:
                    del c_graph[rootPathNode]

            spurPath, cost = get_shortest_path(c_graph, spur, end)
            total_path = rootPath + spurPath
            if total_path not in b:
                b.append(total_path)
                tr = tuple(rootPath)
                t_c = 0
                if tr in costs:
                    t_c = costs[tr]
                else:
                    for num in range(1,len(tr)):
                        t_c += graph[tr[num-1]][tr[num]]
                costs[tuple(total_path)] = cost + t_c
        if len(b) == 0:
            break
        b.sort(key=lambda x: costs[tuple(x)])
        path = b.pop(0)
        if costs[tuple(path)] > short_cost:
            print(costs[tuple(path)])
            print(short_cost)
            print("path is longer !")
            print(len(a))
            break
        a.insert(k,path)
    output = set()
    for el in a:
        for p_el in el:
            output.add((p_el[0], p_el[1]))
    print(len(output))
    f.close()

if __name__ == '__main__':
    main()