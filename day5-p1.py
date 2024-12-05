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
        for i in range(len(ar)-1, -1, -1):
            if len(to_check) == 0:
                to_check.add(ar[i])
                s: set = rules.get(ar[i])
                if s is not None:
                    not_allowed.update(s.difference(to_check))
            else:
                s: set = rules.get(ar[i])
                if s is None:
                    s = set()
                #if len(s.intersection(not_allowed)) != 0:
                if ar[i] in not_allowed:
                    break
                not_allowed.update(s.difference(to_check))
        else:
            total += ar[floor(len(ar)/2)]
    print(total)
    f.close()

if __name__ == '__main__':
    main()