

def main():
    f = open('day24-input.txt')
    known = {}
    while True:
        line = f.readline()
        if line == '\n':
            break
        data = line.split(':')
        known[data[0]] = int(data[1])
    gates = []
    wanted = set()
    for line in f.readlines():
        gate, result = line.split('->')
        res = result.strip()
        gates.append((tuple(gate.split()), res))
        if res[0] == 'z':
            wanted.add(res)

    f.close()
    while not all((x in known for x in wanted)):
        done = True
        for g in gates:
            if g[0][0] in known and g[0][2] in known and g[1] not in known:
                done = False
                match g[0][1]:
                    case 'XOR':
                        known[g[1]] = known[g[0][0]] ^ known[g[0][2]]
                    case 'OR':
                        known[g[1]] = known[g[0][0]] | known[g[0][2]]
                    case 'AND':
                        known[g[1]] = known[g[0][0]] & known[g[0][2]]
        if done:
            break
    print(known)
    print(gates)
    end = []
    for el in sorted(wanted, reverse=True):
        if el not in known:
            print('ERROR NOT FOUND')
        end.append(known[el])
    out = 0
    for bit in end:
        out = (out << 1) | bit
    print(out)


if __name__ == '__main__':
    main()