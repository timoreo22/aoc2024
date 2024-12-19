from typing import TypeAlias
from tqdm import tqdm
from functools import cache
IndexType: TypeAlias = dict[str, 'IndexType']


def count_valid(pattern, index):
    if len(pattern) == 0:
        if '' not in index:
            return -999999999
        return 0
    if pattern[0] in index:
        m = count_valid(pattern[1:], index[pattern[0]])
        if m < 0:
            if '' in index:
                return 1
            else:
                return m
        else:
            return 1 + m
    if '' not in index:
        return -999999999
    else:
        return 0

@cache
def find_pattern(total, pattern):
    if len(total) == 0:
        return 1
    count = 0
    for p in pattern:
        if total[:len(p)] == p:
            count += find_pattern(total[len(p):], pattern)
    return count


def main():
    f = open('day19-input.txt')
    patterns = f.readline()
    f.readline()
    to_find = [x for x in f.readlines()]
    f.close()
    index: IndexType = {}
    patterns_combined = []
    for pattern in patterns.split(','):
        cur_idx: IndexType = index
        patterns_combined.append(pattern.strip())
        for c in pattern.strip():
            if c not in cur_idx:
                cur_idx[c] = {}
            cur_idx = cur_idx[c]
        cur_idx[''] = {}
    print(index)
    total = 0
    to_use = tuple(patterns_combined)
    for pattern in tqdm(to_find):
        pattern = pattern.strip()
        total += find_pattern(pattern, to_use)
        #m = count_valid(pattern, index)
        #pattern = pattern[m:]
        #while m > 0 and len(pattern) > 0:
        #    m = count_valid(pattern, index)
        #    if m > 0:
        #        pattern = pattern[m:]
        #if len(pattern) == 0:
        #    total += 1
    print(total)
if __name__ == '__main__':
    main()