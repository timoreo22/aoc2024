def main():
    f = open('day4-input.txt')
    ar = [list(x.strip()) for x in f.readlines()]
    f.close()
    dim_x = len(ar)
    dim_y = len(ar[0])
    word = 'XMAS'
    l_word = len(word)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0
    for i in range(dim_x):
        for j in range(dim_y):
            if ar[i][j] != word[0]:
                continue
            for dire in dirs:
                # start search
                c_x = i + dire[0]
                c_y = j + dire[1]
                k = 1
                while k < l_word:
                    if c_x >= dim_x or c_x < 0 or c_y >= dim_y or c_y < 0:
                        break
                    if ar[c_x][c_y] != word[k]:
                        break
                    c_x += dire[0]
                    c_y += dire[1]
                    k += 1
                else:
                    total += 1

    print(total)

if __name__ == '__main__':
    main()