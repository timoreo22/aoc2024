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
        o =  translate(g[1])
        outs[o] = id(g)
        ins[id(g)].append(g[0][0])
        ins[id(g)].append(g[0][2])
        inp = '|'.join(( '<' + g[0][0] + '>' + g[0][0], '<' + g[0][2] + '>' + g[0][2]))
        out = '<' + o + '>' + o
        print(id(g),'[label="{{' + inp +'}|' + g[0][1] +'|{' + out + '}}"];', file=graph)
    for i in ins:
        for fr in ins[i]:
            if fr in outs:
                print(str(outs[fr]) + ':' + fr + '->' + str(i) + ':' + fr +  ';',file=graph)
    print("}", file=graph)
    graph.close()
    os.system("dot -Tsvg graph.dot -o graph-orig.svg")


def translate(fr):
    if fr == 'z21':
        fr = 'shh'
    elif fr == 'shh':
        fr = 'z21'
    elif fr == 'z33':
        fr = 'dqr'
    elif fr == 'dqr':
        fr = 'z33'
    #extra infos
    elif fr == 'z39':
        fr = 'pfw'
    elif fr == 'pfw':
        fr = 'z39'
    return fr


if __name__ == '__main__':
    main()