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
                    #build_graph((px,py), valid.difference(start), end, d, graph)


# def minDist(distances: dict[tuple[int,int, tuple[int,int]], int | float], visited: dict[tuple[int,int, tuple[int,int]], bool]) -> tuple[int,int, tuple[int,int]] | None:
#     m = 1e9
#     idx = None
#     for v in visited.keys():
#         if distances[v] < m and visited[v] == False:
#             m = distances[v]
#             idx = v
#     return idx


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
    #for _ in range(len(visited)):
    #    m = minDist(distances, visited)
    #    if m is None:
            #print("Panic !!!!")
    #        continue
    #    visited[m] = True
    #    for v in visited.keys():
    #        if v in graph[m] and graph[m][(v[0], v[1])] > 0 and visited[(v[0],v[1],m[2])] == False and distances[(v[0],v[1],m[2])] > distances[m] + graph[m][(v[0], v[1])]:
    #            distances[v] = distances[m] + graph[m][(v[0], v[1])]
    #print(distances)
    #return distances

# mem: dict[tuple[tuple[int,int],tuple[int,int]],int] = {}
# cache_hits = 0
# cache_miss = 0
# def search_end(start, current_dir, valid: set[tuple[int,int]], target) -> int | float:
#     global cache_hits, cache_miss
#     if (start, current_dir) in mem:
#         cache_hits += 1
#         return mem[(start,current_dir)]
#     cache_miss += 1
#     dire = [current_dir, (current_dir[1], current_dir[0]), (-current_dir[1], -current_dir[0])]
#     score = 0
#     best_alt = 1e9
#     while True:
#         found = 0
#         for d in dire:
#             px = start[0] + d[0]
#             py = start[1] + d[1]
#             if (px,py) in valid:
#                 found += 1
#                 valid.remove((px,py))
#                 if d != current_dir:
#                     best_alt = min(search_end((px,py), d, valid.copy(), target) + 1001 + score, best_alt)
#                 else:
#                     score += 1
#                     start = (start[0] + d[0], start[1] + d[1])
#                 if (px,py) == target:
#                     mem[(start, current_dir)] = min(score + 1, best_alt)
#                     return min(score + 1, best_alt)
#         if found == 0:
#             break
#     mem[(start,current_dir)] = best_alt
#     return best_alt
#
# def timstra_old(start, valid, target):
#     idire = [(-1,0),(0,1),(1,0),(0,-1)]
#     cur_dir = (1,0)
#     score = 1e9
#     for d in idire:
#         px = start[0] + d[0]
#         py = start[1] + d[1]
#         if (px,py) in valid:
#             if d != cur_dir:
#                 score = min(search_end((px, py), d, valid.copy(), target) + 1000, score)
#             else:
#                 score = min(search_end((px,py), d, valid.copy(), target), score)
#     return score




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
    # for d in dire:
    #     px = start[0] + d[0]
    #     py = start[1] + d[1]
    #     if (px,py) in valid:
    #         graph[(start[0], start[1], d)][(px,py)] = 1
    #         build_graph(valid.difference(start), graph)
    print(graph)
    print(start)
    print(graph[(1, start[1], (1,0))])
    print("Points:",len(valid))
    dist, prev = timstra((start[0], start[1], (1,0)), graph)
    # for d in dire:
    #     s = []
    #     u = (end[0], end[1], d)
    #     if prev[u] is not None or u == (start[0], start[1], (1,0)):
    #         while u is not None:
    #             s.insert(0, u)
    #             u = prev[u]
    #     print(s)
    for d in dire:
        print(dist[(end[0],end[1], d)])
    #print("Score: ", dist)
    #print("Hits: ",cache_hits)
    #print("Miss: ",cache_miss)
    f.close()

if __name__ == '__main__':
    main()