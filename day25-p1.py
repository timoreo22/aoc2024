def main():
    f = open('day25-input.txt')
    # read all lines, figure out if lock or key, add to list, for each lock try every key
    # lock = top line filled
    # key = top line empty
    first = True
    lock = False
    locks = []
    keys = []
    current = [0,0,0,0,0]
    total_size = 7
    for line in f.readlines():
        if line == '\n':
            if lock:
                locks.append(tuple(current))
            else:
                keys.append(tuple(total_size - x for x in current))
            current = [0,0,0,0,0]
            first = True
            lock = False
            continue
        if first:
            first = False
            if line[0] == '#':
                lock = True
        for i, c in enumerate(line):
            if c == '#':
                current[i] += 1
    valid = 0
    for lock in locks:
        for key in keys:
            good = True
            for i in range(len(lock)):
                if lock[i] > key[i]:
                    good = False
                    break
            if good:
                valid += 1
    print(valid)



    f.close()

if __name__ == '__main__':
    main()