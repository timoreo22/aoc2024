from sympy import *
from sympy.logic.boolalg import *
def main():
    init_printing(use_unicode=True)
    f = open('day24-input.txt')
    values = {}
    n_x = []
    n_y = []
    while True:
        line = f.readline()
        if line == '\n':
            break
        data = line.split(':')
        val = symbols(data[0])
        values[data[0]] = val

        if data[0][0] == 'x':
            n_x.append(val)
        else:
            n_y.append(val)
    gates = IndexedBase('gates') #'gates', IntSort(), BitVecSort(1))
    wanted = {}
    solv = []
    # generate pairs
    # todo add range ?
    pairs = [(Idx('x_' + str(i)), Idx(' y_' + str(i))) for i in range(4)]
    # preconditions
    flattened = [p for pr in pairs for p in pr]
    for i,el in enumerate(flattened):
        for j,x in enumerate(flattened):
            if i != j:
                pass#solv.append(Unequality(el, x))

    count = 0
    for line in f.readlines():
        gate, result = line.split('->')
        res = result.strip()
        i1, logic, i2 = gate.split()
        if i1 not in values:
            values[i1] = symbols(i1)
        if i2 not in values:
            values[i2] = symbols(i2)
        if res not in values:
            values[res] = symbols(res)
        val = values[res]
        for p in pairs:
            val = ITE(Eq(p[0], count, evaluate=False), gates[p[1],0], ITE(Eq(p[1], count, evaluate=False),gates[p[0],0], val))
        match logic:
            case 'XOR':
                solv.append(Eq(Xor(values[i1], values[i2]), val, evaluate=False))
            case 'OR':
                solv.append(Eq(Or(values[i1] , values[i2]), val, evaluate=False))
            case 'AND':
                solv.append(Eq(And(values[i1] , values[i2]), val, evaluate=False))
        solv.append(Eq(gates[count,0], values[res]))
        count += 1
        if res[0] == 'z':
            wanted[res] = values[res]
    f.close()
    # final assumption, the circuit should be equal to +
    print(count)
    solv.extend([Lt(p, count) for pr in pairs for p in pr])
    solv.extend([Ge(p,0) for pr in pairs for p in pr])
    n_z = [wanted[x] for x in sorted(wanted)]
    n_c = [False]
    for i in range(len(n_x)):
        sum = Xor(n_x[i] , n_y[i])
        carry = And(n_x[i] , n_y[i])
        s2 = Xor(n_c[i] , sum)
        c2 = And(n_c[i] , sum)
        n_c.append(Or(carry , c2))
        solv.append(Eq(s2, n_z[i], evaluate=False))
    # poor man's ForAll, the real one seems to use up ALL of my ram
    #for x in range(2**len(n_x)):
    #    for y in range(2**len(n_y)):
    #        solv.add(Implies(And(out_x == x, out_y == y), out_z == x + y))
    #solv.add(out_z == out_x + out_y)
    #solv.add(ForAll(n_x + n_y,out_z == out_x + out_y))
    print('here we go')
    print(solv)
    print(len(solv))
    fr = solv.pop(0)
    res = fr
    for el in solv:
       res = And(res, el)
    print(gateinputcount(res))
    solv.insert(0, fr)
    sol = nsolve(solv, flattened, (100,) * len(flattened), dict=True)
    print(sol)
    print(solv.check())
    print(solv.model())
    for p in pairs:
        print(solv.model()[p[0]], '<=>', solv.model()[p[1]])
    print(solv.model().eval(out_y))
    print(solv.model().eval(out_x))
    print(solv.model().eval(out_z))

if __name__ == '__main__':
    main()