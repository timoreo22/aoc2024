from math import floor


def main():
    f = open("day5-input.txt")
    line = f.readline()
    #if i see key
    rules = {}
    while len(line.strip()) > 1:
        first, second = [int(x) for x in line.split('|')]
        ar = rules.setdefault(first, set())
        ar.add(second)
        line = f.readline()

    # go through the list in reverse order
    # skip first
    total = 0
    for line in f.readlines():
        ar = [int(x) for x in line.strip().split(',')]
        to_check = set()
        not_allowed = set()
        why = {}
        out_of_order = False
        i = len(ar) -1
        while i >= 0:
            if len(to_check) == 0:
                to_check.add(ar[i])
                s: set = rules.get(ar[i])
                if s is not None:
                    sub = s.difference(to_check).difference(not_allowed)
                    for el in sub:
                        why[el] = i
                    not_allowed.update(sub)
            else:
                s: set = rules.get(ar[i])
                if s is None:
                    s = set()
                if ar[i] in not_allowed:
                    other = why[ar[i]]
                    ar[other], ar[i] = ar[i], ar[other]
                    i = len(ar)
                    to_check = set()
                    not_allowed = set()
                    why = {}
                    out_of_order = True
                else:
                    sub = s.difference(to_check).difference(not_allowed)
                    for el in sub:
                        why[el] = i
                    not_allowed.update(sub)
            i -= 1
        if out_of_order:
            total += ar[floor(len(ar) / 2)]

    print(total)
    f.close()

if __name__ == '__main__':
    main()