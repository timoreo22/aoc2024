from z3 import *

def main():
    set_param(proof=True)
    f = open('day24-input.txt')
    values = {}
    n_x = []
    n_y = []
    while True:
        line = f.readline()
        if line == '\n':
            break
        data = line.split(':')
        val = BitVec(data[0],1)
        values[data[0]] = val

        if data[0][0] == 'x':
            n_x.append(val)
        else:
            n_y.append(val)
    gates = Array('gates', IntSort(), BitVecSort(1))
    wanted = {}
    solv = Solver()
    # generate pairs
    pairs = [Ints('x_' + str(i) + ' y_' + str(i)) for i in range(4)]
    # preconditions

    solv.add(Distinct([p for pr in pairs for p in pr]))

    count = 0
    for line in f.readlines():
        gate, result = line.split('->')
        res = result.strip()
        i1, logic, i2 = gate.split()
        if i1 not in values:
            values[i1] = BitVec(i1, 1)
        if i2 not in values:
            values[i2] = BitVec(i2, 1)
        if res not in values:
            values[res] = BitVec(res, 1)
        val = values[res]
        for p in pairs:
            val = If(p[0] == count, gates[p[1]], If(p[1] == count, gates[p[0]], val))
        match logic:
            case 'XOR':
                solv.add(values[i1] ^ values[i2] == val)
            case 'OR':
                solv.add(values[i1] | values[i2] == val)
            case 'AND':
                solv.add(values[i1] & values[i2] == val)
        gates = Store(gates, count, values[res])
        count += 1
        if res[0] == 'z':
            wanted[res] = values[res]
    f.close()
    # final assumption, the circuit should be equal to +
    print(count)
    solv.add(*[p < count for pr in pairs for p in pr])
    solv.add(*[p >= 0 for pr in pairs for p in pr])
    out_x = BV2Int(Concat(list(reversed(n_x))))
    out_y = BV2Int(Concat(list(reversed(n_y))))
    # order z bits
    end = []
    for el in sorted(wanted, reverse=True):
        end.append(wanted[el])
    out_z = BV2Int(Concat(end))
    # poor man's ForAll, the real one seems to use up ALL of my ram
    for x in range(2**len(n_x)):
        for y in range(2**len(n_y)):
            solv.add(Implies(And(out_x == x, out_y == y), out_z == x + y))
    #solv.add(out_z == out_x + out_y)
    #solv.add(ForAll(n_x + n_y,out_z == out_x + out_y))
    print('here we go')
    print(solv.check())
    print(solv.model())
    for p in pairs:
        print(solv.model()[p[0]], '<=>', solv.model()[p[1]])
    print(solv.model().eval(out_y))
    print(solv.model().eval(out_x))
    print(solv.model().eval(out_z))

if __name__ == '__main__':
    main()