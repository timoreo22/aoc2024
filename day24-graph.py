import os
from collections import defaultdict


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
    # try to display the graph
    graph = open("graph.dot", "w")
    print('digraph {', file=graph)
    print("node [shape=record];", file=graph)
    # display every gate
    outs = {}
    ins = defaultdict(lambda: [])
    # add input nodes
    for k in known:
        outs[k] = id(k)
        out = '<' + k + '>' + k
        print('{rank = source;', id(k),'[label="' + out + '"];}', file=graph)
    # add output nodes
    for k in wanted:
        ins[id(k)].append(k)
        out = '<' + k + '>' + k
        print('{rank = sink;',id(k), '[label="' + out + '"];}', file=graph)
    for g in gates:
        outs[g[1]] = id(g)
        ins[id(g)].append(g[0][0])
        ins[id(g)].append(g[0][2])
        inp = '|'.join(( '<' + g[0][0] + '>' + g[0][0], '<' + g[0][2] + '>' + g[0][2]))
        out = '<' + g[1] + '>' + g[1]
        print(id(g),'[label="{{' + inp +'}|' + g[0][1] +'|{' + out + '}}"];', file=graph)
    for i in ins:
        for fr in ins[i]:
            if fr in outs:
                print(str(outs[fr]) + ':' + fr + '->' + str(i) + ':' + fr +  ';',file=graph)
    print("}", file=graph)
    graph.close()
    os.system("dot -Tsvg graph.dot -o graph.svg")


if __name__ == '__main__':
    main()