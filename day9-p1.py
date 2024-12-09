from math import ceil

def main():
    f = open('day9-input.txt', 'r')
    line = [int(x) for x in f.read().strip()]
    free_idx = 1
    free_left = line[free_idx]
    idx = len(line) - 1 - (1 - (len(line) % 2))
    file_id = ceil(len(line) / 2) - 1
    total_count = line[0]
    total = 0
    last_alloc = 0
    # idx must be even, free_idx must be odd
    while idx > free_idx:
        block_count = line[idx]
        while block_count > 0:
            if free_left == 0:
                free_idx += 2
                total_count += line[free_idx - 1]
                free_left = line[free_idx]
            to_del = min(free_left, block_count)
            if idx <= free_idx:
                last_alloc += to_del
                total_count -= line[free_idx - 1]
            else:
                last_alloc = to_del

            tmp = to_del
            while tmp > 0:
                total += file_id * total_count
                total_count += 1
                tmp -= 1
            block_count -= to_del
            free_left -= to_del
        file_id -= 1
        idx -= 2
    total_count -= last_alloc + 1
    # finish off counting
    while idx > 0:
        tmp = line[idx]
        while tmp > 0:
            total += file_id * total_count
            total_count -= 1
            tmp -= 1
        total_count -= line[idx - 1]
        file_id -= 1
        idx -= 2
    print(total)
    f.close()

if __name__ == '__main__':
    main()