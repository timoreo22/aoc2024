import random


def main():
    f = open('day24-input.txt')
    known = {}
    n_x = []
    n_y = []
    while True:
        line = f.readline()
        if line == '\n':
            break
        data = line.split(':')
        val = random.randint(0,1) #int(data[1])
        known[data[0]] = val
        if data[0][0] == 'x':
            n_x.insert(0,val)
        else:
            n_y.insert(0,val)
    print(known)
    expected = bv_to_int(n_x) + bv_to_int(n_y)
    gates: dict[str, tuple[str,str,str]] = {}
    wanted = set()
    for line in f.readlines():
        gate, result = line.split('->')
        res = result.strip()
        spl = gate.split()
        gates[res] = (spl[0],spl[1],spl[2])
        if res[0] == 'z':
            wanted.add(res)
    # TODO remove, applying swaps
    gates['z39'], gates['pfw'] = gates['pfw'], gates['z39']
    gates['z33'], gates['dqr'] = gates['dqr'], gates['z33']
    gates['dtk'], gates['vgs'] = gates['vgs'], gates['dtk']
    gates['z21'], gates['shh'] = gates['shh'], gates['z21']

    f.close()
    output = []
    out = compute_gates(gates, known, wanted)
    # mismatches = out ^ expected
    if out == expected:
        exit(0) # all done !
    # check from MSB onwards
    bit = 45
    cin_nets = set()
    while bit > 0:
        zpad = f'{bit:02}'
        print(zpad)
        if bit == 45:
            check_carry(cin_nets, gates, gates['z' + zpad], zpad)
        else:
            # should be a xor
            in1, gate, in2 = gates['z' + zpad]
            if gate == 'XOR':
                if in1 in cin_nets:
                    check_carry(cin_nets, gates, gates[in1], zpad)
                    check_adder(gates[in2], zpad)

                else:
                    if in2 in cin_nets:
                        check_carry(cin_nets, gates, gates[in2], zpad)
                        check_adder(gates[in1], zpad)
                    else:
                        print(gates[in2], in2, 'is fucky')

            else:
                print(in1, gate, in2, 'z' + zpad, 'is fucky')
        bit -= 1


def check_adder(gate, zpad):
    l, g, r = gate
    if g != 'XOR':
        print(gate, 'is fucky')
    elif not ((l == 'x' + zpad and r == 'y' + zpad) or (l == 'y' + zpad and r == 'x' + zpad)):
        print(gate, 'is fucky')


def check_carry(cin_nets, gates, inp_g, zpad):
    in1, gate, in2 = inp_g
    if gate == 'OR':
        g1 = gates[in1]
        g2 = gates[in2]
        # check if g1 is other
        if g1[0][0] == 'x' or g1[0][0] == 'y':
            # assume g1 is other
            check_other(g1)
            # assume g2 is half
            check_half(cin_nets, g2, gates, zpad)
        else:
            # assume g2 is other
            check_other(g2)
            # assume g1 is half
            check_half(cin_nets, g1, gates, zpad)

    else:
        print(in1, gate, in2, 'is fucky')


def check_half(cin_nets, g2, gates, zpad):
    l, g, r = g2
    if g == 'AND':
        # one side is OR (cin), other is it
        # check if l is XOR
        if gates[l][1] == 'XOR':
            # l is it
            check_last(gates, l, zpad)
            # other is cin
            cin_nets.add(r)
        else:
            check_last(gates, r, zpad)
            cin_nets.add(l)
    else:
        print(g2, 'is fucky')


def check_last(gates, r, zpad):
    # r should be it
    zpad = f'{int(zpad) - 1:02}'
    if gates[r][1] == 'XOR':
        # must both be direct input on same rank as output
        if not ((gates[r][0] == 'x' + zpad and gates[r][2] == 'y' + zpad) or (
                gates[r][0] == 'y' + zpad and gates[r][2] == 'x' + zpad)):
            print(gates[r], 'is fucky')

    else:
        print(gates[r], 'is fucky')


def check_other(gate):
    l, g, r = gate
    # should be zpad -1, but no need to check
    if not ((l[0] == 'x' or l[0] == 'y') and g == 'AND' and (r[0] == 'x' or r[0] == 'y')):
        print(l, g, r, 'is fucky')


def compute_gates(gates: dict[str, tuple[str,str,str]], kn: dict[str, int], wanted: set[str]):
    known = kn.copy()
    while not all((x in known for x in wanted)):
        done = True
        for g in gates:
            gate = gates[g]
            if gate[0] in known and gate[2] in known and g not in known:
                done = False
                match gate[1]:
                    case 'XOR':
                        known[g] = known[gate[0]] ^ known[gate[2]]
                    case 'OR':
                        known[g] = known[gate[0]] | known[gate[2]]
                    case 'AND':
                        known[g] = known[gate[0]] & known[gate[2]]
        if done:
            break
    end = []
    for el in sorted(wanted, reverse=True):
        if el not in known:
            print('ERROR NOT FOUND')
        end.append(known[el])
    return bv_to_int(end)


def bv_to_int(ar: list[int]) -> int:
    out = 0
    for bit in ar:
        out = (out << 1) | bit
    return out


if __name__ == '__main__':
    main()