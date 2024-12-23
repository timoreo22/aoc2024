from collections import defaultdict
from itertools import combinations

def main():
    f = open('day23-input.txt')
    nets = defaultdict(lambda: set())
    for line in f.readlines():
        data = line.split('-')
        c1 = data[0].strip()
        c2 = data[1].strip()
        nets[c1].add(c2)
        nets[c1].add(c1)
        nets[c2].add(c1)
        nets[c2].add(c2)
    f.close()
    combos = set()
    for s in nets.values():
        for c in combinations(s, 3):
            for el in c:
                if el[0] == 't':
                    combo = frozenset(c)
                    # is valid combo ?
                    has_all = True
                    for thing in c:
                        has_all &= nets[thing].issuperset(combo)
                    if has_all:
                        combos.add(combo)
                    break
    print(len(combos))

if __name__ == '__main__':
    main()