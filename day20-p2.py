from collections import Counter
from tqdm import tqdm, trange

counter = Counter()
cheats = set()
dire = [(-1, 0), (0, 1), (1, 0), (0, -1)]
path_info = {}
end = ()

def main():
    global end
    f = open('day20-input.txt')
    start = ()
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
    f.close()
    path_info[start] = 0
    cur = start
    cost = 1
    while cur != end:
        for d in dire:
            px = cur[0] + d[0]
            py = cur[1] + d[1]
            if (px,py) not in path_info and (px,py) in valid:
                cur = (px,py)
                path_info[cur] = cost
                cost += 1
                break

    total = 0
    for p in tqdm(path_info.keys()):
        cx = p[0]
        cy = p[1]
        for px in range(cx - 21, cx + 21):
            for py in range(cy - 21, cy + 21):
                if ((cx, cy), (px, py)) in cheats or (px,py) not in path_info:
                    continue
                score = abs(px - cx) + abs(py - cy)
                if score <= 20 and abs(path_info[(cx,cy)] - path_info[(px,py)]) - score >= 100:
                    cheats.add(((cx, cy), (px, py)))
                    cheats.add(((px, py), (cx, cy)))
                    #counter[abs(path_info[(cx,cy)] - path_info[(px,py)]) - score] += 1
                    total += 1
        #find_cheats(cx, cy, p, 2)
    print(total)
    #print(counter)
    #print(cheats)
    #print(path_info)

already_seen = set()

# def find_cheats(cx, cy, p, left):
#     if left <= 0:
#         return
#     if (cx,cy,p,left) in already_seen:
#         return
#     already_seen.add((cx,cy,p,left))
#     for d in dire:
#         px = cx + d[0]
#         py = cy + d[0]
#         # check cheat
#         if ((p[0], p[1]), (px, py)) not in cheats and (px, py) in path_info and left == 1:
#             saved = path_info[(px, py)] - path_info[p] - (3 - left)
#             cheats.add(((p[0], p[1]), (px, py)))
#             if saved > 0:
#                 # print(left, saved)
#                 counter[saved] += 1
#
#         if (px, py) != end and px > 0 and py > 0:
#             find_cheats(px, py, p, left - 1)


if __name__ == '__main__':
    main()