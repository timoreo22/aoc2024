from math import ceil

def main():
    f = open('day9-input.txt', 'r')
    line = [int(x) for x in f.read().strip()]
    idx = len(line) - 1 - (1 - (len(line) % 2))
    file_id = ceil(len(line) / 2) - 1
    total = 0
    free_blocks: dict[int, tuple[int,int]] = {}
    ignore_ids = set()
    while idx > 0:
        block_count = line[idx]
        free_idx = 1
        free_left = line[free_idx]
        total_count = line[0]
        while free_idx < idx:
            if free_left >= block_count:
                if total_count in free_blocks:
                    free_left -= free_blocks[total_count][0]
                    total_count += free_blocks[total_count][0]
                else:
                    free_blocks[total_count] = (block_count, file_id)
                    ignore_ids.add(file_id)
                    tmp = block_count
                    while tmp > 0:
                        total += total_count * file_id
                        total_count += 1
                        tmp -= 1
                    total_count -= block_count
                    break
            else:
                total_count += free_left
                total_count += line[free_idx + 1]
                free_idx += 2
                if free_idx < idx:
                    free_left = line[free_idx]
        file_id -= 1
        idx -= 2
    idx = 2
    file_id = 1
    total_count = line[0]

    while idx < len(line):
        total_count += line[idx - 1]
        block_count = line[idx]
        if file_id not in ignore_ids:
            tmp = block_count
            while tmp > 0:
                total += total_count * file_id
                total_count += 1
                tmp -= 1
        else:
            total_count += block_count
        idx += 2
        file_id += 1
    print(total)
    f.close()

if __name__ == '__main__':
    main()