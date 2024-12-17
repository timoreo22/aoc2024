from z3 import *

def store_to_array(s):
    lent = s[0]
    output = []
    for i in range(simplify(lent).as_long()):
        output.append(simplify(s[i + 1]))
    return output

magic_output = 0
BITS_IN_NUM = 64
def main():
    f = open('day17-ex.txt')
    for _ in range(4):
        f.readline()

    p_instructions = [int(x) for x in f.readline().split()[1].split(',')]
    print(p_instructions)
    ctx = Context()
    instructions = Array('instructions', BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx))
    idx = 0
    for i in p_instructions:
        instructions = Store(instructions, idx, i)
        idx += 1
    f.close()

    def get_combo(i, a, b, c):
        return If(i <= 3, i, If(i == 4, a, If(i == 5, b, If(i == 6, c, 1e9))))

    do_ins = RecFunction('do_ins', BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx), ArraySort(BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx)))

    def append_array(el, ar: ArrayRef) -> ArrayRef:
        i = ar[0] + 1
        return Store(Store(ar,0,i),i,el)
    def do_instruction(rip, a, b, c):
        global magic_output
        output = Store(Array('output_' + str(magic_output), BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx)), 0, 0)
        magic_output += 1
        return If(rip > len(p_instructions) - 1, output,
           If(instructions[rip] == 0, do_ins(rip + 2, a / (1 << get_combo(instructions[rip + 1], a, b, c)), b, c),
              If(instructions[rip] == 1,do_ins(rip + 2, a, b ^ instructions[rip + 1], c),
                 If(instructions[rip] == 2, do_ins(rip + 2, a, get_combo(instructions[rip + 1], a, b, c) % 8, c),
                    If(instructions[rip] == 3, do_ins(If(a != 0, instructions[rip + 1], rip + 2), a, b, c),
                       If(instructions[rip] == 4, do_ins(rip + 2, a, b ^ c, c),
                          If(instructions[rip] == 5, append_array(get_combo(instructions[rip + 1], a, b, c) % 8,do_ins(rip + 2, a,b,c)),
                             If(instructions[rip] == 6, do_ins(rip + 2, a, a / (1 << get_combo(instructions[rip + 1], a, b, c)), c),
                                If(instructions[rip] == 7, do_ins(rip + 2, a, b, a / (1 << get_combo(instructions[rip + 1], a, b, c))),
              Store(output, 0, 69))))))))))

    d_rip,d_a,d_b,d_c = BitVecs('d_rip d_a d_b d_c', BITS_IN_NUM, ctx=ctx)
    def_ins = simplify(do_instruction(d_rip,d_a,d_b,d_c))
    # print(def_ins)
    RecAddDefinition(do_ins, [d_rip,d_a,d_b,d_c], def_ins)
    print('TEST', store_to_array(simplify(do_ins(0,0,0,0))))
    print('TEST', store_to_array(simplify(do_ins(0,117440,0,0))))
    print('TEST', store_to_array(simplify(do_ins(0,42,0,0))))
    s = Solver(ctx=ctx)
    a = BitVec('a', BITS_IN_NUM, ctx=ctx)
    sol = simplify(do_ins(0,a,0,0))
    #s.add(a < 1000000)
    # s.add(a == 117440)
    #s.add(a >= 117440) # 117440
    #s.add(a < 117442)
    #s.add(sol[0] == 6)
    s.add(instructions[5] == simplify(instructions[5]))
    s.add(instructions[4] == simplify(instructions[4]))
    s.add(instructions[3] == simplify(instructions[3]))
    s.add(instructions[2] == simplify(instructions[2]))
    s.add(instructions[1] == simplify(instructions[1]))
    s.add(instructions[0] == simplify(instructions[0]))

    s.add(sol[1] == simplify(instructions[5]))
    s.add(sol[2] == simplify(instructions[4]))
    s.add(sol[3] == simplify(instructions[3]))
    s.add(sol[4] == simplify(instructions[2]))
    s.add(sol[5] == simplify(instructions[1]))
    s.add(sol[6] == simplify(instructions[0]))
    k = Array('k', BitVecSort(BITS_IN_NUM, ctx=ctx), BitVecSort(BITS_IN_NUM, ctx=ctx))
    # s.minimize(a)
    s.add(k == sol)
    #s.add(do_ins(0,0,0,0) != k)
    #s.add(6 == k[0])
    #for i in range(len(p_instructions)):
    #    s.add(k[i+1] == simplify(instructions[len(p_instructions) - i - 1]))
    print(s)
    if s.check() == sat:
        print('WORKING')
        print(s.model().eval(a))
        val = s.model().eval(k)
        print("len", simplify(val[0]))
        print(p_instructions)
        print(store_to_array(val))
        for i in range(1,len(p_instructions) + 1):
            print(simplify(val[i]),',', end='', sep='')
        print()
        print(s.model())
        #print(s.model())
    else:
        print('Not solvable !')

if __name__ == '__main__':
    main()