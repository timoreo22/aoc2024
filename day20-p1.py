def main():
    f = open('day20-input.txt')
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
    f.close()
    dire = [(-1,0),(0,1),(1,0),(0,-1)]
    path_info = {start: 0}
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
    cost -= 1
    # c = Counter()
    total = 0
    for p in path_info.keys():
        for d1 in dire:
            for d2 in dire:
                px = p[0] + d1[0] + d2[0]
                py = p[1] + d1[1] + d2[1]
                if (px,py) in path_info:
                    saved = path_info[(px,py)] - path_info[p] - 2
                    if saved >= 100:
                        #c[saved] += 1
                        total += 1
    print(total)
    #print(path_info)


if __name__ == '__main__':
    main()