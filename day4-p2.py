def main():
    f = open('day4-input.txt')
    ar = [list(x.strip()) for x in f.readlines()]
    f.close()
    dim_x = len(ar)
    dim_y = len(ar[0])
    # A is middle
    dirs = [(-1,-1),(1,1),(1,-1),(-1,1)]
    total = 0
    for i in range(dim_x):
        for j in range(dim_y):
            if ar[i][j] != 'A':
                continue
            k = 0
            to_find = None
            for dire in dirs:
                # start search
                c_x = i + dire[0]
                c_y = j + dire[1]
                if c_x >= dim_x or c_x < 0 or c_y >= dim_y or c_y < 0:
                    break
                w = ar[c_x][c_y]
                if to_find is None and (w == 'M' or w == 'S'):
                    if w == 'M':
                        to_find = 'S'
                    else:
                        to_find = 'M'
                    k += 1
                elif to_find is not None:
                    if w == to_find:
                        k += 1
                        to_find = None
                else:
                    break
            if k == len(dirs):
                total += 1
    print(total)

if __name__ == '__main__':
    main()